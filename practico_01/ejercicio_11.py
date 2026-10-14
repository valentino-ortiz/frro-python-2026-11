"""Sum, Compresión de Listas, Map, Filter, Reduce."""

from typing import Iterable


def suma_cubo_pares_for(numeros: Iterable[int]) -> int:
    """Toma una lista de números, los eleva al cubo, y devuelve la suma de
    los elementos pares.

    Restricción: Utilizar dos bucles for, uno para elevar al cubo y otro para
    separar los pares.
    """

    # Dos bucles separados, como pide el enunciado: primero se arma la lista de
    # cubos y después se acumulan solo los pares.
    cubos = []

    for n in numeros:
        cubos.append(n ** 3)

    suma = 0

    for c in cubos:
        if c % 2 == 0:
            suma = suma + c

    return suma


# NO MODIFICAR - INICIO
assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################


def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
    """Re-Escribir utilizando comprension de listas (debe resolverse en 1 línea)
    y la función built-in sum.

    Referencia: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """

    # La comprensión reemplaza a los dos bucles en una línea; con corchetes se
    # arma la lista completa antes de sumar (la versión con generador no).
    return sum([n**3 for n in numeros if (n**3) % 2 == 0])


# NO MODIFICAR - INICIO
assert suma_cubo_pares_sum_list([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################


def suma_cubo_pares_sum_gen(numeros: Iterable[int]) -> int:
    """ Re-Escribir utilizando expresiones generadoras (debe resolverse en 1 línea)
    y la función sum.
    Referencia: https://docs.python.org/3/reference/expressions.html#generator-expressions
    """

    # Igual que la comprensión pero sin corchetes: sum consume los valores de a
    # uno y no se crea la lista intermedia en memoria.
    return sum(n**3 for n in numeros if (n**3) % 2 == 0)


# NO MODIFICAR - INICIO
assert suma_cubo_pares_sum_gen([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################

# PARTE 2
# A continuación se introduce el concepto de Lambdas (Funciones anónimas),
# Escribir las funciones lambdas que corresponda en cada línea
# Referencia: https://docs.python.org/3/reference/expressions.html#lambda

numeros = [1, 2, 3, 4, 5, 6]


# Escribir una función lambda que eleve los elementos al cubo

# map aplica la lambda a cada elemento; list materializa el resultado porque
# map devuelve un iterador y los asserts comparan contra una lista.
numeros_al_cubo = list(map(lambda x: x**3, numeros))

# Escribir una función lambda que permita filtrar todos los elementos pares

# filter conserva solo los elementos para los que la lambda devuelve True.
numeros_al_cubo_pares = list(filter(lambda x: x % 2 == 0, numeros_al_cubo))

# Escribir una función Lambda que sume todos los elementos

from functools import reduce

# reduce va acumulando de a pares con la lambda hasta quedarse con un solo valor.
suma_numeros_al_cubo_pares = reduce(lambda a, b: a + b, numeros_al_cubo_pares)


# Escribir una función Lambda que permita ordenar los elementos de la numeros
# en base a si son pares o impares

# La clave vale False para impares y True para pares; como False < True y sorted
# es estable, los impares quedan primero conservando su orden original.
numeros_ordenada = sorted(numeros, key=lambda x: x % 2 == 0)


# NO MODIFICAR - INICIO
assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
assert numeros_al_cubo_pares == [8, 64, 216]
assert suma_numeros_al_cubo_pares == 288
assert numeros_ordenada == [1, 3, 5, 2, 4, 6]
# NO MODIFICAR - FIN
