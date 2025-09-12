# Outils de mesure de performances

- `generate_datasets.py` : crée des jeux de données sous `data/` (aléatoire, trié, inversé, presque trié, peu de valeurs distinctes) pour différentes tailles.
- `bench_tri.py` : exécute les algorithmes de tri des apprenants sur ces jeux et mesure **temps d'exécution** et **nombre de comparaisons**.

Le comptage des comparaisons est réalisé en enveloppant les entiers dans un type `Comparable` qui incrémente un compteur à chaque opération de comparaison (`<, <=, >, >=, ==`). Aucune modification n'est requise dans le code des apprenants : leurs comparaisons habituelles déclenchent le comptage.

## Utilisation
```bash
python tools/generate_datasets.py
python tools/bench_tri.py --repeats 5 --plot
```


