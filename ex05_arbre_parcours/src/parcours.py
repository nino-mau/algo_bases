from __future__ import annotations

from typing import List, Optional

from common.tree import Node


def parcours_prefixe(racine: Optional[Node]) -> List[object]:
    """
    Parcours préfixe (ou parcours en profondeur d'abord, version préfixe) :
    - Si le nœud racine est None, retourne une liste vide.
    - Ajoute la valeur du nœud racine à la liste de résultat.
    - Parcourt récursivement le sous-arbre gauche en utilisant la même méthode.
    - Parcourt récursivement le sous-arbre droit en utilisant la même méthode.
    - Combine les résultats et retourne la liste complète.
    """

    res = []
    currentNode = racine

    if currentNode is None:
        return []

    res.append(currentNode.value)

    left = parcours_prefixe(currentNode.left)
    right = parcours_prefixe(currentNode.right)

    print(left)
    print(right)

    return [*res, *left, *right]


def parcours_infixe(racine: Optional[Node]) -> List[object]:
    """
    Parcours infixe :
    - Si le nœud racine est None, retourne une liste vide.
    - Parcourt récursivement le sous-arbre gauche en utilisant la même méthode.
    - Ajoute la valeur du nœud racine à la liste de résultat.
    - Parcourt récursivement le sous-arbre droit en utilisant la même méthode.
    - Combine les résultats et retourne la liste complète.
    """
    res = []
    currentNode = racine

    if currentNode is None:
        return []

    left = parcours_infixe(currentNode.left)

    res.extend(left)
    print("Left: ", left)
    print("Res: ", res)

    res.append(currentNode.value)
    print("Current: ", currentNode.value)
    print("Res: ", res)

    right = parcours_infixe(currentNode.right)

    res.extend(right)
    print("Right: ", right)
    print("Res: ", res)

    return res


def parcours_suffixe(racine: Optional[Node]) -> List[object]:
    """
    Parcours suffixe (parcours post-ordre) :
    - Si le nœud racine est None, retourne une liste vide.
    - Parcourt récursivement le sous-arbre gauche en utilisant la même méthode.
    - Parcourt récursivement le sous-arbre droit en utilisant la même méthode.
    - Ajoute la valeur du nœud racine à la liste de résultat.
    - Combine les résultats et retourne la liste complète.
    """
    res = []
    currentNode = racine

    if currentNode is None:
        return []

    left = parcours_suffixe(currentNode.left)
    res.extend(left)
    print("Left: ", left)
    print("Res: ", res)

    right = parcours_suffixe(currentNode.right)
    res.extend(right)
    print("Right: ", right)
    print("Res: ", res)

    res.append(currentNode.value)
    print("Current: ", currentNode.value)
    print("Res: ", res)

    return res


def parcours_largeur(racine: Optional[Node]) -> List[object]:
    """
    Parcours en largeur (utilisation d'une file) :
    - Si le nœud racine est None, retourne une liste vide.
    - Initialise une queue (file) contenant le nœud racine.
    - Pendant que la queue n'est pas vide :
        - Extraire le premier élément de la queue.
        - Ajouter la valeur de ce nœud à la liste de résultat.
        - Ajouter les sous-arbres gauche et droit à la fin de la queue s'ils ne sont pas None.
    - Retourne la liste de résultat.
    """
    queue = []
    res = []
    current = racine

    if current is None:
        return []

    queue.append(current)

    while len(queue):
        print("Queue:", queue)
        first: Node = queue[0]
        queue.remove(first)

        res.append(first.value)

        if first.left:
            queue.append(first.left)
        if first.right:
            queue.append(first.right)

    print("Res:", res)
    return res


def parcours_dfs(racine: Optional[Node]) -> List[object]:
    """
    Parcours en profondeur (Depth-First Search, basé sur une pile) :
    - Si le nœud racine est None, retourne une liste vide.
    - Initialise une pile contenant uniquement le nœud racine.
    - Pendant que la pile n'est pas vide :
        - Extraire le nœud en haut de la pile.
        - Ajouter la valeur de ce nœud à la liste de résultat.
        - Ajouter les sous-arbres droit et gauche (dans cet ordre) à la pile si présents.
    - Retourne la liste de résultat.
    """
    res = []
    current = racine

    if current is None:
        return []

    stack = [current]

    while len(stack):
        top: Node = stack.pop()

        res.append(top.value)

        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)

    return res


def parcours_bfs(racine: Optional[Node]) -> List[object]:
    """
    Parcours en largeur (Breadth-First Search, basé sur une file) :
    - Si le nœud racine est None, retourne une liste vide.
    - Initialise une file contenant uniquement le nœud racine.
    - Pendant que la file n'est pas vide :
        - Extraire le nœud en tête de la file.
        - Ajouter la valeur de ce nœud à la liste de résultat.
        - Ajouter les sous-arbres gauche et droit (dans cet ordre) à la file s'ils ne sont pas None.
    - Retourne la liste de résultat.
    """
    res = []
    current = racine

    if current is None:
        return []

    queue = [current]

    while len(queue):
        first: Node = queue[0]
        queue.remove(first)

        res.append(first.value)

        if first.left:
            queue.append(first.left)
        if first.right:
            queue.append(first.right)

    return res
