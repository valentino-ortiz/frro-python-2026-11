"""Base de Datos - Creación de Clase en ORM"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Socio(Base):
    """Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, unico)
        - dni: entero (unico)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'

    # El atributo se llama "id" porque así lo usan los asserts de ejercicio_02,
    # pero la columna se llama "id_socio" como pide el enunciado. La clave
    # primaria ya es única, por eso no hace falta repetir unique=True.
    id = Column('id_socio', Integer, primary_key=True, autoincrement=True)
    dni = Column(Integer, unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
