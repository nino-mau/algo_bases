from __future__ import annotations


def somme_pairs(nums: list[int]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs de la liste donnée.
    res = 0
    for n in nums:
        if n % 2 == 0:
            res += n
    return res


def compter_occurrences(items: list[int], valeur: int) -> int:
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences de `valeur` dans la liste `items`.
    res = 0
    for n in items:
        if n == valeur:
            res += 1
    return res


def table_multiplication(n: int) -> list[int]:
    # TODO: Implémentez la fonction pour retourner la table de multiplication de `n` (jusqu'à 10 inclus).
    res = []
    for i in range(1, 11):
        res.append(n * i)
    return res


def trouver_maximum(nums: list[int]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner la valeur maximale dans la liste.
    max = 0
    for n in range(0, len(nums) - 1):
        currentItem = nums[n]
        nextItem = nums[n + 1]
        if currentItem > nextItem:
            max = currentItem
    return max


def calculer_moyenne(nums: list[int]) -> float:
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des valeurs dans la liste.
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)


def compter_negatifs(nums: list[int]) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre d'entiers négatifs dans la liste.
    res = 0
    for n in nums:
        if isinstance(n, int):
            if n < 0:
                res += 1
    return res


def compter_mots(phrase: str) -> int:
    # TODO: Implémentez une fonction pour compter le nombre de mots dans une chaîne de caractères donnée.
    return len(phrase.split())


def trouver_plus_long(items: list[str]) -> str:
    # TODO: Implémentez une fonction pour trouver et retourner le mot le plus long dans une liste de chaînes de caractères.
    res = ""
    for n in range(0, len(items) - 1):
        currentItem = len(items[n])
        nextItem = len(items[n + 1])
        if currentItem > nextItem:
            res = items[n]
    return res


def convertir_majuscule(items: str) -> str:
    # TODO: Implémentez une fonction pour convertir toutes les chaînes de la liste en majuscules.
    return items.upper()


def compter_mots_commencant_par(items: str, lettre: str) -> int:
    # TODO: Implémentez une fonction pour compter les mots commençant par une lettre donnée.
    res = 0
    for n in items.split():
        if n[0] == lettre:
            res += 1
    return res


def trouver_mot_finissant_par(items: str, suffixe: str) -> list[str]:
    # TODO: Implémentez une fonction pour trouver tous les mots qui se terminent par un suffixe donné dans la liste.
    res = []
    for n in items.split():
        if n.endswith(suffixe):
            res.append(n)
    return res


def compter_caracteres(s: str, char: str) -> int:
    # TODO: Implémentez une fonction pour compter le nombre d'occurences du caractère char et retourner le nombre total.
    res = 0
    for n in s:
        if n == char:
            res += 1
    return res


def inverser_chaine(s: str) -> str:
    # TODO: Implémentez une fonction pour inverser et retourner la chaîne de caractères donnée.
    res = []
    for n in reversed(s):
        res.append(n)
    return "".join(res)


def trouver_occurrences_chaine(s: str, c: str) -> int:
    # TODO: Implémentez une fonction pour compter les occurrences d'un caractère donné dans une chaîne.
    return s.count(c)


def somme_pairs_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un tuple donné.
    res = 0
    for n in nums:
        if n % 2 == 0:
            res += n
    return res


def compter_occurrences_tuples(items: tuple[int, ...], valeur: int) -> int:
    # TODO: Implémentez la fonction pour compter le nombre d'occurrences d'une valeur dans un tuple donné.
    res = 0
    for n in items:
        if n == valeur:
            res += 1
    return res


def table_multiplication_tuples(n: int) -> tuple[int, ...]:
    # TODO: Implémentez la fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de tuple.
    res = []
    for i in range(1, 11):
        res.append(n * i)
    return tuple(res)


def trouver_maximum_tuples(nums: tuple[int, ...]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un tuple.
    max = 0
    for n in range(0, len(nums) - 1):
        currentItem = nums[n]
        nextItem = nums[n + 1]
        if currentItem > nextItem:
            max = currentItem
    return max


def calculer_moyenne_tuples(nums: tuple[int, ...]) -> float:
    # TODO: Implémentez une fonction pour calculer et retourner la moyenne des nombres dans un tuple.
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)


# sets


def somme_pairs_sets(nums: set[int]) -> int:
    # TODO: Implémentez la fonction pour calculer la somme de tous les nombres pairs dans un set donné.
    res = 0
    for n in nums:
        if n % 2 == 0:
            res += n
    return res


def compter_occurrences_sets(items: set[int], valeur: int) -> int:
    # TODO: Cette fonction vérifiera simplement si `valeur` existe puisque les sets ne permettent pas les doublons.
    res = 0
    for n in items:
        if n == valeur:
            res += 1
    return res


def table_multiplication_sets(n: int) -> set[int]:
    # TODO: Implémentez une fonction pour retourner la table de multiplication (jusqu'à 10 inclus) sous forme de set.
    res = []
    for i in range(1, 11):
        res.append(n * i)
    return set(res)


def trouver_maximum_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour trouver et retourner le nombre maximum d'un set.
    return max(nums)


def compter_negatifs_sets(nums: set[int]) -> int:
    # TODO: Implémentez une fonction pour compter et retourner le nombre de nombres négatifs dans un set.
    res = 0
    for n in nums:
        if isinstance(n, int):
            if n < 0:
                res += 1
    return res


# dictionnaires


def ajouter_element(d: dict, cle: str, valeur: any) -> dict:
    # TODO: Implémentez une fonction pour ajouter une clé et sa valeur dans un dictionnaire.
    d[cle] = valeur
    return d


def supprimer_element(d: dict, cle: str) -> dict:
    # TODO: Implémentez une fonction pour supprimer une clé et sa valeur d'un dictionnaire.
    d.pop(cle)
    return d


def fusionner_dictionnaires(d1: dict, d2: dict) -> dict:
    # TODO: Implémentez une fonction qui fusionne deux dictionnaires et renvoie le résultat.
    # Les valeurs de `d2` remplaceront celles de `d1` en cas de doublons.
    d1.update(d2)
    return d1


def inverser_dictionnaire(d: dict) -> dict:
    # TODO: Implémentez une fonction pour inverser un dictionnaire, échangeant les clés et les valeurs.
    # Note: Si des valeurs duplicatées existent, une erreur ou un comportement spécifique doit être défini.
    res = {v: k for k, v in d.items()}
    return res


def compter_valeurs(d: dict) -> int:
    # TODO: Implémentez une fonction pour compter combien de paires clé-valeur sont dans le dictionnaire.
    return len(d.values())


def trouver_valeur_maximale(d: dict) -> any:
    # TODO: Implémentez une fonction pour trouver et retourner la valeur la plus grande dans un dictionnaire.
    return max(d.values())


def trouver_cle_par_valeur(d: dict, valeur: any) -> list[str]:
    # TODO: Implémentez une fonction pour retourner une liste de toutes les clés correspondant à une valeur donnée.
    res = ""
    for k, v in d.items():
        if v == valeur:
            res = k
    return res


def verifier_cle_existe(d: dict, cle: str) -> bool:
    # TODO: Implémentez une fonction qui vérifie si une clé existe dans le dictionnaire.
    res = False
    for k, v in d.items():
        if k == cle:
            res = True
    return res


def valeurs_uniques(d: dict) -> set:
    # TODO: Implémentez une fonction qui retourne toutes les valeurs uniques dans un dictionnaire sous forme de set.
    values = d.values()
    return set(values)


def mettre_a_jour_valeur(d: dict, cle: str, nouvelle_valeur: any) -> dict:
    # TODO: Implémentez une fonction pour mettre à jour une valeur associée à une clé existante ou en ajouter une nouvelle.
    if d[cle]:
        d[cle] = nouvelle_valeur
    else:
        d.update({cle: nouvelle_valeur})
    return d
