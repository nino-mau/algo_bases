from ex04_tri.src.exercices import (
tri_bulle,
    tri_insertion, 
    tri_selection, 
tri_shell,
tri_tas,
    tri_rapide
)

CASES = [
    [],
    [1],
    [3,2,1],
    [5,1,4,2,8],
    [2,2,2],
    [9, -1, 3, 0, 2, -5],
    [13, -5, 7, 0, 22, -11, 45, 19, 28, -9, -6, 12, 31, 4, 8, -3, 17, 26, -19, 30],
]


def test_bulle():
    for case in CASES:
        assert tri_bulle(case) == sorted(case)


def test_insertion():
    for case in CASES:
        assert tri_insertion(case) == sorted(case)
        assert case == case  # pas de mutation


def test_selection():
    for case in CASES:
        assert tri_selection(case) == sorted(case)


def test_shell():
    for case in CASES:
        assert tri_shell(case) == sorted(case)


def test_tas():
    for case in CASES:
        assert tri_tas(case) == sorted(case)


def test_rapide():
    for case in CASES:
        assert tri_rapide(case) == sorted(case)
