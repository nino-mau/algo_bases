import pytest

from ex01_variables_conditions.src.exercices import (
    somme,
    produit,
    est_pair,
    est_voyelle,
    calcul_reduction,
    est_bissextile,
    racine_carree,
    maximum_trois,
    factorielle,
    convertir_en_binaire
)


def test_somme():
    assert somme(2, 3) == 5
    assert somme(-2, 3) == 1
    assert somme(0, 0) == 0


def test_produit():
    assert produit(3, 4) == 12
    assert produit(-3, 4) == -12
    assert produit(0, 4) == 0


def test_est_pair():
    assert est_pair(4) is True
    assert est_pair(3) is False
    assert est_pair(0) is True


def test_est_voyelle():
    assert est_voyelle('a') is True
    assert est_voyelle('b') is False
    assert est_voyelle('E') is True
    assert est_voyelle('z') is False


def test_calcul_reduction_simples():
    assert calcul_reduction(100.0, 0.0) == 100.0
    assert calcul_reduction(100.0, 10.0) == 90.0
    assert calcul_reduction(50.0, 50.0) == 25.0


def test_calcul_reduction_bornes():
    assert calcul_reduction(0.0, 10.0) == 0.0
    assert calcul_reduction(100.0, 200.0) == 0.0  # pas négatif
    with pytest.raises(ValueError):
        calcul_reduction(-1.0, 10.0)


def test_est_bissextile():
    assert est_bissextile(2000) is True
    assert est_bissextile(1900) is False
    assert est_bissextile(2024) is True
    assert est_bissextile(2023) is False


def test_racine_carree():
    assert racine_carree(4) == 2
    assert racine_carree(0) == 0
    assert racine_carree(9) == 3
    with pytest.raises(ValueError):
        racine_carree(-4)


def test_maximum_trois():
    assert maximum_trois(1, 2, 3) == 3
    assert maximum_trois(3, 2, 1) == 3
    assert maximum_trois(-5, -2, -3) == -2


def test_factorielle():
    assert factorielle(5) == 120
    assert factorielle(0) == 1
    assert factorielle(1) == 1
    with pytest.raises(ValueError):
        factorielle(-1)


def test_convertir_en_binaire():
    assert convertir_en_binaire(5) == '101'
    assert convertir_en_binaire(0) == '0'
    assert convertir_en_binaire(10) == '1010'
