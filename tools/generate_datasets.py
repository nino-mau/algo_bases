from __future__ import annotations
import os, random, argparse, json
from pathlib import Path

SIZES = [100, 1000, 3000, 10000]
SEED = 1337

def almost_sorted(n: int) -> list[int]:
    arr = list(range(n))
    # introduire quelques inversions locales
    for i in range(0, n, max(1, n//20)):
        if i+1 < n:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def few_unique(n: int) -> list[int]:
    vals = [0, 1, 2, 3, 4]
    return [random.choice(vals) for _ in range(n)]

def save_list(path: Path, arr: list[int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(",".join(map(str, arr)) + "\n")

def main(out_dir: str):
    random.seed(SEED)
    base = Path(out_dir)
    patterns = {}
    for n in SIZES:
        patterns[f"random_{n}"] = [random.randint(-10_000, 10_000) for _ in range(n)]
        patterns[f"sorted_{n}"] = list(range(n))
        patterns[f"reversed_{n}"] = list(range(n, 0, -1))
        patterns[f"almost_sorted_{n}"] = almost_sorted(n)
        patterns[f"few_unique_{n}"] = few_unique(n)
    for name, arr in patterns.items():
        save_list(base / f"{name}.txt", arr)
    print(f"Généré {len(patterns)} fichiers dans {base}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data", help="Dossier de sortie (par défaut: data)")
    args = parser.parse_args()
    main(args.out)
