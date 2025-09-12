from common.tree import Node
from ex05_arbre_parcours.src.parcours import (
    parcours_prefixe, 
    parcours_infixe, 
    parcours_suffixe, 
    parcours_largeur,
parcours_dfs,
parcours_bfs
)


def test_parcours_sur_vide():
    arbre_vide = None
    arbre_feuille = Node("A")
    arbre_complet = Node("A", Node("B", Node("D"), Node("E")), Node("C", Node("F"), Node("G")))

    assert parcours_prefixe(arbre_vide) == []
    assert parcours_infixe(arbre_vide) == []
    assert parcours_suffixe(arbre_vide) == []
    assert parcours_largeur(arbre_vide) == []
    assert parcours_dfs(arbre_vide) == []
    assert parcours_bfs(arbre_vide) == []

    assert parcours_prefixe(arbre_feuille) == ["A"]
    assert parcours_infixe(arbre_feuille) == ["A"]
    assert parcours_suffixe(arbre_feuille) == ["A"]
    assert parcours_largeur(arbre_feuille) == ["A"]
    assert parcours_dfs(arbre_feuille) == ["A"]
    assert parcours_bfs(arbre_feuille) == []

    assert parcours_prefixe(arbre_complet) == ["A", "B", "D", "E", "C", "F", "G"]
    assert parcours_infixe(arbre_complet) == ["D", "B", "E", "A", "F", "C", "G"]
    assert parcours_suffixe(arbre_complet) == ["D", "E", "B", "F", "G", "C", "A"]
    assert parcours_largeur(arbre_complet) == ["A", "B", "C", "D", "E", "F", "G"]
    assert parcours_dfs(arbre_complet) == ["A", "B", "D", "E", "C", "F", "G"]
    assert parcours_bfs(arbre_complet) == ["A", "B", "C", "D", "E", "F", "G"]
