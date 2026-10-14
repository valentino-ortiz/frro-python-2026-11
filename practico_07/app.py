"""
TP7 - Capa de Presentación: Gestión de Socios
Aplicación web en Flask que interactúa exclusivamente con la Capa de Negocio (NegocioSocio).
"""

import os
import sys

# Asegurar que el directorio raíz del repositorio esté en el path de Python
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PRACTICO_05_DIR = os.path.abspath(os.path.join(BASE_DIR, "practico_05"))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
if PRACTICO_05_DIR not in sys.path:
    sys.path.insert(0, PRACTICO_05_DIR)

import tempfile

from flask import Flask, flash, redirect, render_template, request, url_for

# Aislar la importación de practico_06/practico_05 en un directorio temporal para
# evitar que las pruebas a nivel de módulo de ejercicio_02.py colisionen con la base
# real o la borren al importar.
_prev_cwd = os.getcwd()
with tempfile.TemporaryDirectory() as _tmp_dir:
    os.chdir(_tmp_dir)
    try:
        from practico_05.ejercicio_01 import Socio
        from practico_06.capa_negocio import (
            DniRepetido,
            LongitudInvalida,
            MaximoAlcanzado,
            NegocioSocio,
        )
    finally:
        os.chdir(_prev_cwd)

app = Flask(__name__)
app.secret_key = "soporte_python_tp7_secret_key"

negocio = NegocioSocio()


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Formulario principal: muestra todos los socios en una tabla
    y cuenta con los botones Alta, Baja y Modificar.
    """
    if request.method == "POST":
        accion = request.form.get("accion")
        id_socio_str = request.form.get("id_socio")

        if not id_socio_str:
            flash("Debe seleccionar un socio de la tabla.", "warning")
            return redirect(url_for("index"))

        try:
            id_socio = int(id_socio_str)
        except (ValueError, TypeError):
            flash("Identificador de socio inválido.", "danger")
            return redirect(url_for("index"))

        if accion == "modificar":
            return redirect(url_for("modificar", id_socio=id_socio))
        elif accion == "baja":
            return redirect(url_for("baja", id_socio=id_socio))

    socios = negocio.todos()
    return render_template("index.html", socios=socios)


def es_dni_valido(dni_str):
    """Verifica que el DNI tenga exactamente 8 caracteres numéricos."""
    return len(dni_str) == 8 and dni_str.isdigit()


def dni_disponible(dni, id_socio_actual):
    """Comprueba si el DNI está disponible o si ya pertenece al mismo socio."""
    socio = negocio.buscar_dni(dni)
    return socio is None or socio.id == id_socio_actual


@app.route("/alta", methods=["GET", "POST"])
def alta():
    """
    Alta: abre una página con un formulario con los campos para ingresar
    los datos de socio que incluye 2 botones: Guardar y Cancelar.
    """
    if request.method == "POST":
        dni_str = request.form.get("dni", "").strip()
        nombre = request.form.get("nombre", "").strip()
        apellido = request.form.get("apellido", "").strip()

        # Validación: el DNI debe contener exactamente 8 dígitos numéricos
        if not es_dni_valido(dni_str):
            flash("El DNI debe contener exactamente 8 dígitos numéricos.", "danger")
            return render_template("alta.html", dni=dni_str, nombre=nombre, apellido=apellido)

        dni = int(dni_str)
        socio = Socio(dni=dni, nombre=nombre, apellido=apellido)

        try:
            negocio.alta(socio)
            flash(f"Socio '{nombre} {apellido}' dado de alta exitosamente.", "success")
            return redirect(url_for("index"))
        except DniRepetido:
            flash(f"Error: El DNI {dni} ya se encuentra registrado.", "danger")
        except LongitudInvalida:
            flash("Error: El nombre y el apellido deben tener más de 3 y menos de 15 caracteres.", "danger")
        except MaximoAlcanzado:
            flash("Error: Se ha alcanzado el límite máximo permitido de socios (200).", "danger")
        except Exception as err:
            flash(f"Error inesperado al guardar el socio: {err}", "danger")

        return render_template("alta.html", dni=dni_str, nombre=nombre, apellido=apellido)

    return render_template("alta.html")


@app.route("/modificar/<int:id_socio>", methods=["GET", "POST"])
def modificar(id_socio):
    """
    Modificar: abre un formulario con los campos con los datos del socio seleccionado
    e incluye 2 botones: Aceptar y Cancelar.
    """
    socio = negocio.buscar(id_socio)
    if socio is None:
        flash(f"No se encontró ningún socio con ID #{id_socio}.", "warning")
        return redirect(url_for("index"))

    if request.method == "POST":
        dni_str = request.form.get("dni", "").strip()
        nombre = request.form.get("nombre", "").strip()
        apellido = request.form.get("apellido", "").strip()

        if not es_dni_valido(dni_str):
            flash("El DNI debe contener exactamente 8 dígitos numéricos.", "danger")
            socio_formulario = Socio(id=id_socio, dni=dni_str, nombre=nombre, apellido=apellido)
            return render_template("modificar.html", socio=socio_formulario)

        dni = int(dni_str)
        if not dni_disponible(dni, id_socio):
            flash(f"Error: Ya existe otro socio registrado con el DNI {dni}.", "danger")
            socio_formulario = Socio(id=id_socio, dni=dni, nombre=nombre, apellido=apellido)
            return render_template("modificar.html", socio=socio_formulario)

        socio_a_modificar = Socio(id=id_socio, dni=dni, nombre=nombre, apellido=apellido)

        try:
            negocio.modificacion(socio_a_modificar)
            flash(f"Socio '{nombre} {apellido}' (ID #{id_socio}) modificado exitosamente.", "success")
            return redirect(url_for("index"))
        except LongitudInvalida:
            flash("Error: El nombre y el apellido deben tener más de 3 y menos de 15 caracteres.", "danger")
        except Exception as err:
            flash(f"Error al modificar el socio: {err}", "danger")

        socio_formulario = Socio(id=id_socio, dni=dni, nombre=nombre, apellido=apellido)
        return render_template("modificar.html", socio=socio_formulario)

    return render_template("modificar.html", socio=socio)


@app.route("/baja/<int:id_socio>", methods=["GET", "POST"])
def baja(id_socio):
    """
    Baja: da de baja el socio seleccionado.
    """
    exito = negocio.baja(id_socio)
    if exito:
        flash(f"Socio ID #{id_socio} dado de baja exitosamente.", "success")
    else:
        flash(f"No se pudo dar de baja al socio ID #{id_socio} (no encontrado).", "warning")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
