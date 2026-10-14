"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """

    # IF NOT EXISTS hace que se pueda llamar más de una vez sin error, y se
    # cierra la conexión explícitamente para liberar el archivo .db.
    conexion = sqlite3.connect("personas.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Persona (
            IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre CHAR(30),
            FechaNacimiento DATE,
            DNI INTEGER,
            Altura INTEGER
        )
    """)

    conexion.commit()
    conexion.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""

    # IF EXISTS evita el error si la tabla ya fue borrada (misma idea que en
    # crear_tabla).
    conexion = sqlite3.connect("personas.db")
    cursor = conexion.cursor()

    cursor.execute("DROP TABLE IF EXISTS Persona")

    conexion.commit()
    conexion.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
