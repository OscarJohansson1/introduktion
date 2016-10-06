"""Parsons programming-problem.

Instruktion
===========

All kod som behövs för att lösa uppgiften finns. Raderna behöver byta plats
och indenteras för att få fungerande kod som löser problemet.

Alla docstrings har placerats före kodraderna som ska användas för problemet.

"""



def running_total(numbers):
    """Givet en lista med tal, beräkna den löpande summan."""
    total = []
    current = 0
    for n in numbers:
        current += n
        total.append(current)
    return total
