# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        # Se delega en la capa de datos, que ya devuelve None si no encuentra nada.
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        # Se delega en la capa de datos, que ya devuelve None si no encuentra nada.
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        # Las 3 reglas se validan antes de tocar la base: si alguna falla,
        # levanta su excepcion y el socio nunca se persiste.
        self.regla_1(socio)
        self.regla_2(socio)
        self.regla_3()

        self.datos.alta(socio)
        return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        # La capa de datos ya informa con True/False si el socio existia.
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        # Solo regla_2: el DNI ya es del propio socio (regla_1 lo rechazaria)
        # y modificar no cambia la cantidad de socios (regla_3).
        self.regla_2(socio)

        self.datos.modificacion(socio)
        return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        # Una sola consulta por DNI, en lugar de recorrer todos los socios.
        socio_existente = self.buscar_dni(socio.dni)

        if socio_existente is not None:
            raise DniRepetido()

        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        # Limites estrictos (mas de 3 y menos de 15), tal como pide el enunciado,
        # tomados de las constantes de clase.
        if len(socio.nombre) <= self.MIN_CARACTERES:
            raise LongitudInvalida()

        if len(socio.nombre) >= self.MAX_CARACTERES:
            raise LongitudInvalida()

        if len(socio.apellido) <= self.MIN_CARACTERES:
            raise LongitudInvalida()

        if len(socio.apellido) >= self.MAX_CARACTERES:
            raise LongitudInvalida()

        return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        # Se cuenta en la base en lugar de traer todos los socios; con >= se
        # impide el alta cuando ya se llego al maximo.
        if self.datos.contarSocios() >= self.MAX_SOCIOS:
            raise MaximoAlcanzado()

        return True
