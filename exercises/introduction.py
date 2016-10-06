"""Övningar på introduction."""


def repeat(string, num):
    """Repeterar en sträng (arg 1) num (arg 2) gånger.

    Returnerar en ny sträng eller en tom sträng om num är negativt.
    """
    return string * num


def bouncer(items):
    """Tar bort alla värden i items (arg 1) som evalueras till False."""
    result = []
    for item in items:
        if item:
            result.append(item)
    return result


def rovarsprak(string):
    """Returnerar strängen på rövarspråk.

    * Versaler och gemener ska vara kvar enligt instoppad sträng.

    * Övriga tecken (.,*! etc.) ska vara kvar på samma position.
    `Wikipedia<https://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket>`_
    """
    rovarsprak = []
    konsonant = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k"]
    konsonantStor = ["Q", "W", "R", "T", "P", "S", "D", "F", "G", "H", "J"]
    while len(string) > 0:
        if string[0] == konsonant:
            rovarsprak.append(string)
            rovarsprak.append("o")
            rovarsprak.append(string)
        if string[0] == konsonantStor:
            rovarsprak.append(string)
            rovarsprak.append("O")
            rovarsprak.append(string)
        else:
            rovarsprak.append(string)
    return rovarsprak


def area(width, height):
    """Returnerar arean av en figur med bredden 'width' och höjden 'height'."""
    return width * height


def to_seconds(time):
    """Returnerar en float `time` (timmar) till sekunder."""
    return time * 3600


def is_of_age(age):
    """Returnerar true om 'age' är större eller lika med 18, annars false."""
    result = []
    if age <= 18:
        result.append(True)
        return result
    else:
        result.append(False)
        return result


def vowel(character):
    """Returnerar true om 'character' är en vokal, annart false."""
    pass


def reverse(words):
    """Byter ordning på alla tecken i strängen `words`, returnerar resultatet.

    words = "Hej på dig!" ska till exempel returnera
    strängen "!gid åp jeH".
    """
    result = []
    while len(words) > 0:
        result.insert(0, words)
        if len(words) == 0:
            return result


def overlapping(list1, list2):
    """Returnerar True om listorna har åtminstone ett gemensamt objekt."""
    pass


def is_palindrome(words):
    """Returnerar sant om orden är en palindrom.

    Det vill säga en följd tecken som blir likadan oavsett om den läses
    framlänges eller baklänges, annars false. Ett exempel på palindrom är orden
    'ni talar bra latin' som kan läsas likadant åt båda hållen.
    """
    pass


def what_type(var):
    """Returnerar en sträng med namnet av typen som variabeln 'var' tillhör.

    var = 5 ska till exempel returnera strängen "integer".
    """
    pass


def travel_price(distance, consumtion, price):
    """Beräknar och returnerar priset för en resa.

    Resan är `distance` km lång, och görs med en bil som drar `consumption`
    liter bensin per mil då bensinen kostar `price` kr per liter.
    """
    return (distance / 10) * consumtion * price


def character_frequency(words):
    """Returnerar ett histogram (dictionary).

    Returnerar en dictionary med varje bokstav i strängen `words` som nyckel
    till ett värde av antalet gånger bokstaven uppkommer i stängen.
    """
    pass
