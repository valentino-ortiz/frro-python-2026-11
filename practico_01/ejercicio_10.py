"""For-Else, Any."""

from typing import Iterable


def tiene_pares_basico(numeros: Iterable[int]) -> bool:
    """Toma una lista y devuelve un booleano en función si tiene al menos un
    número par."""

    # El return anticipado corta el recorrido en el primer par; no hace falta
    # contar ni acumular nada.
    for numero in numeros:
        if numero % 2 == 0:
            return True

    return False


# NO MODIFICAR - INICIO
assert tiene_pares_basico([1, 3, 5]) is False
assert tiene_pares_basico([1, 3, 5, 6]) is True
assert tiene_pares_basico([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################


def tiene_pares_for_else(numeros: Iterable[int]) -> bool:
    """Re-Escribir utilizando for-else con dos return y un break.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
    """

    # El else del for solo se ejecuta si el bucle terminó sin break, es decir,
    # si no hubo ningún par. Cumple lo pedido: for-else, dos return y un break.
    for numero in numeros:
        if numero % 2 == 0:
            break
    else:
        return False

    return True


# NO MODIFICAR - INICIO
assert tiene_pares_for_else([1, 3, 5]) is False
assert tiene_pares_for_else([1, 3, 5, 6]) is True
assert tiene_pares_for_else([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################


def tiene_pares_any(numeros: Iterable[int]) -> bool:
    """Re-Escribir utilizando la función any, sin utilizar bucles.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """

    # any con expresión generadora hace el for/break/return de forma implícita
    # y es perezoso: se detiene en el primer par.
    return any(numero % 2 == 0 for numero in numeros)


# NO MODIFICAR - INICIO
assert tiene_pares_any([1, 3, 5]) is False
assert tiene_pares_any([1, 3, 5, 6]) is True
assert tiene_pares_any([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN
