from ex04_tri.src.exercices import (
    tri_bulle,
    tri_insertion,
    tri_selection,
    tri_shell,
    tri_tas,
    tri_rapide,
)

CASES = [
    [],
    [1],
    [3, 2, 1],
    [5, 1, 4, 2, 8],
    [2, 2, 2],
    [9, -1, 3, 0, 2, -5],
    [13, -5, 7, 0, 22, -11, 45, 19, 28, -9, -6, 12, 31, 4, 8, -3, 17, 26, -19, 30],
]

tri_rapide(CASES[2])
