"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    # isinstance es la forma idiomática de chequear el tipo, y alcanza con
    # preguntar por str sin enumerar los tipos numéricos posibles.
    strings = []
    numeros = []

    for elemento in lista:
        if isinstance(elemento, str):
            strings.append(elemento)
        else:
            numeros.append(elemento)

    return strings + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    # Dos comprensiones con la condición complementaria: recorre la lista dos
    # veces pero se lee directo y cada grupo conserva su orden relativo.
    strings = [x for x in lista if isinstance(x, str)]
    numeros = [x for x in lista if not isinstance(x, str)]

    return strings + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    # La key es False para los str y True para el resto; como sorted es
    # estable, los str quedan primero y cada grupo conserva su orden original.
    return sorted(lista, key=lambda x: not isinstance(x, str))


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    # Dos filter con lambdas complementarias; se envuelven en list() porque
    # filter devuelve un iterador perezoso que no se puede concatenar con +.
    strings = list(filter(lambda x: isinstance(x, str), lista))
    numeros = list(filter(lambda x: not isinstance(x, str), lista))

    return strings + numeros


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    # Cada nivel devuelve (strings, numeros) y antepone el primero al grupo
    # que le toca: así se conserva el orden (con resto + [primero] los números
    # quedarían invertidos).
    def separar(elementos):
        if not elementos:
            return [], []

        primero, *resto = elementos
        strings, numeros = separar(resto)

        if isinstance(primero, str):
            return [primero] + strings, numeros
        return strings, [primero] + numeros

    strings, numeros = separar(lista)
    return strings + numeros


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
