"""Parsons programming-problem.

Instruktion
===========

All kod som behövs för att lösa uppgiften finns. Raderna behöver byta plats
och indenteras för att få fungerande kod som löser problemet.

Alla docstrings har placerats före kodraderna som ska användas för problemet.

"""


def find_max(numbers):
    """Givet en lista med heltal, hitta det största och returnera."""
    max_n = numbers[0]
    for n in numbers:
        if n > max_n:
            max_n = n
    return max_n
