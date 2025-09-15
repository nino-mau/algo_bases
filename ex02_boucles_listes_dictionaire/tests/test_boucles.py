from ex02_boucles_listes_dictionaire.src.exercices import (
    somme_pairs,
    compter_occurrences,
    table_multiplication,
    trouver_maximum,
    calculer_moyenne,
    compter_negatifs,
    compter_mots,
    trouver_plus_long,
    convertir_majuscule,
    compter_mots_commencant_par,
    trouver_mot_finissant_par,
    compter_caracteres,
    inverser_chaine,
    trouver_occurrences_chaine,
    somme_pairs_tuples,
    compter_occurrences_tuples,
    table_multiplication_tuples,
    trouver_maximum_tuples,
    calculer_moyenne_tuples,
    somme_pairs_sets,
    compter_occurrences_sets,
    table_multiplication_sets,
    trouver_maximum_sets,
    compter_negatifs_sets,
    ajouter_element,
    supprimer_element,
    fusionner_dictionnaires,
    inverser_dictionnaire,
    compter_valeurs,
    trouver_valeur_maximale,
    trouver_cle_par_valeur,
    verifier_cle_existe,
    valeurs_uniques,
    mettre_a_jour_valeur
)


def test_somme_pairs():
    assert somme_pairs([1, 2, 3, 4, 5, 6]) == 12
    assert somme_pairs([]) == 0
    assert somme_pairs([1, 3, 5]) == 0


def test_compter_occurrences():
    assert compter_occurrences([1, 2, 2, 3, 2], 2) == 3
    assert compter_occurrences([], 7) == 0


def test_table_multiplication():
    assert table_multiplication(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert table_multiplication(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


def test_trouver_maximum():
    assert trouver_maximum([1, 3, 7, 2, 5]) == 7
    assert trouver_maximum([-10, -3, -1, -7]) == -1


def test_calculer_moyenne():
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3.0
    assert calculer_moyenne([]) == 0


def test_compter_negatifs():
    assert compter_negatifs([-1, -2, 3, 4, -5]) == 3
    assert compter_negatifs([1, 2, 3]) == 0


def test_compter_mots():
    assert compter_mots("Bonjour tout le monde") == 4
    assert compter_mots("") == 0


def test_trouver_plus_long():
    assert trouver_plus_long(["chat", "chouette", "chien"]) == "chouette"
    assert trouver_plus_long([]) == ""


def test_convertir_majuscule():
    assert convertir_majuscule("Bonjour tout le monde") == "BONJOUR TOUT LE MONDE"
    assert convertir_majuscule("") == ""


def test_compter_mots_commencant_par():
    assert compter_mots_commencant_par("Bonjour tout le monde", "t") == 1
    assert compter_mots_commencant_par("", "b") == 0


def test_trouver_mot_finissant_par():
    assert trouver_mot_finissant_par("Bonjour tout le monde", "r") == ["Bonjour"]
    assert trouver_mot_finissant_par("Bonjour tout le monde", "out") == ["tout"]
    assert trouver_mot_finissant_par("Bonjour tout le monde", "e") == ["le", "monde"]
    assert trouver_mot_finissant_par("Bonjour tout le monde", "r") == ["Bonjour"]
    assert trouver_mot_finissant_par("", "e") == []


def test_compter_caracteres():
    assert compter_caracteres("Bonjour tout le monde", "o") == 4
    assert compter_caracteres("", "a") == 0


def test_inverser_chaine():
    assert inverser_chaine("Bonjour") == "ruojnoB"
    assert inverser_chaine("") == ""


def test_trouver_occurrences_chaine():
    assert trouver_occurrences_chaine("Bonjour tout le monde", "le") == 1
    assert trouver_occurrences_chaine("abcabcabc", "bc") == 3


def test_somme_pairs_tuples():
    assert somme_pairs_tuples((1, 2, 3, 4, 5, 6)) == 12
    assert somme_pairs_tuples(()) == 0
    assert somme_pairs_tuples((1, 3, 5)) == 0


def test_compter_occurrences_tuples():
    assert compter_occurrences_tuples((1, 2, 2, 3, 2), 2) == 3
    assert compter_occurrences_tuples((), 7) == 0


def test_table_multiplication_tuples():
    assert table_multiplication_tuples(1) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert table_multiplication_tuples(5) == (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)


def test_trouver_maximum_tuples():
    assert trouver_maximum_tuples((1, 3, 7, 2, 5)) == 7
    assert trouver_maximum_tuples((-10, -3, -1, -7)) == -1


def test_calculer_moyenne_tuples():
    assert calculer_moyenne_tuples((1, 2, 3, 4, 5)) == 3.0
    assert calculer_moyenne_tuples(()) == 0


def test_somme_pairs_sets():
    assert somme_pairs_sets({1, 2, 3, 4, 5, 6}) == 12
    assert somme_pairs_sets(set()) == 0
    assert somme_pairs_sets({1, 3, 5}) == 0


def test_compter_occurrences_sets():
    assert compter_occurrences_sets({1, 2, 3, 4}, 2) == 1
    assert compter_occurrences_sets(set(), 7) == 0


def test_table_multiplication_sets():
    assert table_multiplication_sets(1) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    assert table_multiplication_sets(5) == {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}


def test_trouver_maximum_sets():
    assert trouver_maximum_sets({1, 3, 7, 2, 5}) == 7
    assert trouver_maximum_sets({-10, -3, -1, -7}) == -1


def test_compter_negatifs_sets():
    assert compter_negatifs_sets({-1, -2, 3, 4, -5}) == 3
    assert compter_negatifs_sets({1, 2, 3}) == 0


def test_ajouter_element():
    d = {}
    ajouter_element(d, "a", 1)
    assert d == {"a": 1}


def test_supprimer_element():
    d = {"a": 1}
    supprimer_element(d, "a")
    assert d == {}


def test_fusionner_dictionnaires():
    assert fusionner_dictionnaires({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_inverser_dictionnaire():
    assert inverser_dictionnaire({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_compter_valeurs():
    assert compter_valeurs({"a": 1, "b": 1, "c": 2}) == 3
    assert compter_valeurs({}) == 0


def test_trouver_valeur_maximale():
    assert trouver_valeur_maximale({"a": 1, "b": 3, "c": 2}) == 3


def test_trouver_cle_par_valeur():
    assert trouver_cle_par_valeur({"a": 1, "b": 2, "c": 3}, 2) == "b"


def test_verifier_cle_existe():
    assert verifier_cle_existe({"a": 1, "b": 2}, "a") == True
    assert verifier_cle_existe({"a": 1, "b": 2}, "c") == False


def test_valeurs_uniques():
    assert valeurs_uniques({"a": 1, "b": 2, "c": 3}) == {1, 2, 3}


def test_mettre_a_jour_valeur():
    d = {"a": 1}
    mettre_a_jour_valeur(d, "a", 5)
    assert d["a"] == 5
