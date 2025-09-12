from __future__ import annotations

import argparse
import csv
from pathlib import Path

from ex04_tri.src.exercices import (
    tri_bulle,
    tri_insertion,
    tri_selection,
    tri_shell,
    tri_tas,
    tri_rapide,

)
from tools.metrics import bench_sort

ALGOS = {
    "tri_bulle": tri_bulle,
    "tri_insertion": tri_insertion,
    "tri_selection": tri_selection,
    "tri_shell": tri_shell,
    "tri_tas": tri_tas,
    "tri_rapide": tri_rapide,
}


def load_dataset(path: Path) -> list[int]:
    with open(path, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        if not line:
            return []
        return [int(x) for x in line.split(",")]


def main(data_dir: str, repeats: int, do_plot: bool):
    data_path = Path(data_dir)
    files = sorted([p for p in data_path.glob("*.txt")])
    out_dir = Path("out");
    out_dir.mkdir(exist_ok=True)
    csv_path = out_dir / "bench_results.csv"

    rows = []
    for f in files:
        data = load_dataset(f)
        size = len(data)
        for name, fn in ALGOS.items():
            t, comps = bench_sort(fn, data, repeats=repeats)
            rows.append({"dataset": f.name, "n": size, "algo": name, "time_s": f"{t:.6f}", "comparisons": comps})
            print(f"{f.name:25s} | {name:13s} | n={size:6d} | {t:.6f}s | {comps} comps")

    with open(csv_path, "w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=["dataset", "n", "algo", "time_s", "comparisons"])
        writer.writeheader()
        writer.writerows(rows)

    if do_plot:
        try:
            import matplotlib.pyplot as plt
            # tracer uniquement les datasets random_* par n
            random_rows = [r for r in rows if r["dataset"].startswith("random_")]
            ns = sorted(sorted({int(r["n"]) for r in random_rows}))
            for algo in ALGOS.keys():
                xs, ys = [], []
                for n in ns:
                    vals = [float(r["time_s"]) for r in random_rows if r["algo"] == algo and int(r["n"]) == n]
                    if vals:
                        xs.append(n);
                        ys.append(min(vals))
                plt.figure()
                plt.plot(xs, ys, marker="o")
                plt.xlabel("Taille n")
                plt.ylabel("Temps (s)")
                plt.title(f"Performance {algo} sur random_n")
                plt.grid(True, which="both", linestyle=":")
                plt.savefig(out_dir / f"bench_plot_{algo}.png", dpi=150, bbox_inches="tight")
                plt.close()
            print(f"Graphiques enregistrés dans {out_dir}")
        except Exception as e:
            print(f"Plot désactivé (matplotlib indisponible?): {e}")

    print(f"Résultats enregistrés dans {csv_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data", help="Dossier des datasets")
    parser.add_argument("--repeats", type=int, default=5, help="Nombre de répétitions (meilleur temps conservé)")
    parser.add_argument("--plot", action="store_true", help="Génère des graphes (matplotlib)")
    args = parser.parse_args()
    main(args.data, args.repeats, args.plot)
