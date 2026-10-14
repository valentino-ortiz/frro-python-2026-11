"""Base de Datos SQL - Creación de tablas auxiliares"""

import sqlite3

from practico_04.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """

    # La clave foránea se declara en el CREATE TABLE con FOREIGN KEY ...
    # REFERENCES, y IF NOT EXISTS permite llamarla más de una vez sin error.
    with sqlite3.connect("personas.db") as conexion:
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PersonaPeso (
                IdPersona INTEGER,
                Fecha DATE,
                Peso INTEGER,
                FOREIGN KEY (IdPersona) REFERENCES Persona(IdPersona)
            )
        """)


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""

    # IF EXISTS evita el error si la tabla ya fue borrada.
    with sqlite3.connect("personas.db") as conexion:
        cursor = conexion.cursor()

        cursor.execute("DROP TABLE IF EXISTS PersonaPeso")

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
