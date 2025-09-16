from __future__ import annotations
import math


def somme(a: int, b: int) -> int:
    return a + b


def produit(a: int, b: int) -> int:
    return a * b


def est_pair(n: int) -> bool:
    if n % 2 == 0:
        return bool(1)
    else:
        return bool(0)


def est_voyelle(lettre: str) -> bool:
    """Vrai si la lettre est une voyelle."""
    vowels = ["a", "e", "i", "o", "u"]

    for v in vowels:
        if lettre == v:
            return bool(1)
        elif lettre == v.upper():
            return bool(1)

    return bool(0)


def calcul_reduction(prix: float, taux: float) -> float:
    remise = (prix / 100) * taux
    if prix < 0:
        raise ValueError
    if (prix - remise) <= 0:
        return 0
    return prix - remise


def est_bissextile(annee: int) -> bool:
    """Vrai si année bissextile (Grégorien).
    Une année est bissextile si elle est divisible par 4.
    Cependant, elle n'est pas bissextile si elle est divisible par 100, sauf si elle est aussi divisible par 400.
    Par exemple :
        - 2000 est bissextile (divisible par 400).
        - 1900 n'est pas bissextile (divisible par 100 mais pas par 400).
        - 2004 est bissextile (divisible par 4 mais pas par 100).
    """
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def racine_carree(x: float) -> float:
    """Retourne la racine carrée d'un nombre."""
    return math.sqrt(x)
    # TODO
    raise NotImplementedError


def maximum_trois(a: int, b: int, c: int) -> int:
    """Renvoie le maximum de trois valeurs sans utiliser max()."""
    # TODO
    max = 0
    if (a > b) and (a > c):
        max = a
    elif (b > a) and (b > c):
        max = b
    elif (c > a) and (c > b):
        max = c
    return max


def factorielle(n: int) -> int:
    """Retourne la factorielle d'un entier.
    1. Vérifier si n est un nombre négatif :
       - Si oui, lever une exception avec un message d'erreur approprié.
    2. Initialiser une variable résultat à 1.
    3. Pour chaque valeur i de 1 à n inclus :
       - Multiplier le résultat actuel par i.
    4. Retourner le résultat.
    """
    if n < 0:
        raise ValueError
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def convertir_en_binaire(n: int) -> str:
    """Convertit un entier en représentation binaire."""
    return bin(n)[2:]
