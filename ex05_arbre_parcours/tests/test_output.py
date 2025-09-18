from common.tree import Node
from ex05_arbre_parcours.src.parcours import (
    parcours_prefixe,
    parcours_infixe,
    parcours_suffixe,
    parcours_largeur,
    parcours_dfs,
    parcours_bfs,
)

arbre_vide = None
arbre_feuille = Node("A")
arbre_complet = Node(
    "A", Node("B", Node("D"), Node("E")), Node("C", Node("F"), Node("G"))
)

print(parcours_prefixe(arbre_vide))
