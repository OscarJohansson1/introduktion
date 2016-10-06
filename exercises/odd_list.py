"""Parsons programming-problem.

Instruktion
===========

All kod som behövs för att lösa uppgiften finns. Raderna behöver byta plats
och indenteras för att få fungerande kod som löser problemet.

Alla docstrings har placerats före kodraderna som ska användas för problemet.

"""


def odd_list(l):
    """Givet en lista, returnera alla värden på udda positioner."""
    result = []
    index = 0
    for item in l:
        if index % 2 == 1:
            result.append(item)
        index += 1
    return result
