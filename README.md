# Projet d'algorithmie – Exercices progressifs & tests automatiques (v2)

Cette version corrige les **noms de packages** (compatibles import Python) et ajoute un **kit de benchmarks** avec des **jeux de données** pour comparer les performances, notamment des tris.

## Prérequis
- Python 3.10+
- `pip`

## Installation
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer les tests
```bash
pytest -q
```

## Benchmarks de performance (tris)
```bash
# Générer/rafraîchir les jeux de données
python tools/generate_datasets.py

# Lancer le benchmark des tris (temps + comparaisons)
python tools/bench_tri.py

# Résultats
# - out/bench_results.csv : tableau des mesures
# - out/bench_plot.png    : courbe temps(n) par algorithme (optionnel si matplotlib installé)
```
# algo_bases
