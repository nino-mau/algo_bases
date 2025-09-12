# 04 – Algorithmes de tri

Objectif : implémenter insertion, sélection, rapide (sans muter la liste d'entrée).
Puis comparer les performances via `tools/bench_tri.py`.

## Ressources pour comprendre les algorithmes

Voici une liste de ressources utiles pour mieux comprendre les algorithmes présents dans `src/exercices` :

- **Tri par insertion** :
    - Fonctionnement : Le tri par insertion parcourt la liste élément par élément et insère chaque valeur à sa position
      correcte dans une sous-liste triée, en décalant les éléments si nécessaire.
    - Vidéo explicative : [Tri par insertion (YouTube - Français)](https://www.youtube.com/watch?v=ROalU379l3U)
    - Pseudocode (en
      anglais) : [GeeksforGeeks - Insertion Sort Pseudocode](https://www.geeksforgeeks.org/insertion-sort/)
    - Schéma et illustration : [Insertion Sort Animation (VisuAlgo)](https://visualgo.net/en/sorting)

- **Tri par sélection** :
    - Fonctionnement : Le tri par sélection trouve à chaque itération l'élément le plus petit de la liste non triée et
      le place à la fin de la liste triée, en répétant ce processus jusqu'à ce que la liste soit entièrement triée.
    - Vidéo explicative : [Tri par sélection (YouTube - Français)](https://www.youtube.com/watch?v=Ns4TPTC8whw)
    - Ressources détaillées : [Selection Sort (Wikipedia)](https://fr.wikipedia.org/wiki/Tri_par_s%C3%A9lection)
    - Illustration visuelle : [Selection Sort in Action (VisuAlgo)](https://visualgo.net/en/sorting)

- **Tri rapide (Quicksort)** :
    - Fonctionnement : Le tri rapide divise récursivement la liste en deux sous-listes autour d'un pivot, plaçant les
      éléments plus petits à gauche et les plus grands à droite, jusqu'à obtenir une liste triée.
    - Introduction en vidéo : [Tri rapide - Quicksort (YouTube - Français)](https://www.youtube.com/watch?v=MZaf_9IZCrc)
    - Pseudocode avec
      explications : [Quicksort Overview (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/quick-sort)
    - Visualisation étape par étape : [Quicksort Visualization (VisuAlgo)](https://visualgo.net/en/sorting)

- **Tri par bulle** :
    - Fonctionnement : Le tri par bulle compare et échange les éléments adjacents pour les placer dans l'ordre, en
      répétant ce processus jusqu'à ce que tous les éléments soient triés.
    - Vidéo explicative : [Tri à bulles (YouTube - Français)](https://www.youtube.com/watch?v=lyZQPjUT5B4)
    - Pseudocode détaillé : [Bubble Sort (GeeksforGeeks)](https://www.geeksforgeeks.org/bubble-sort/)
    - Démonstration animée : [Bubble Sort Animation (VisuAlgo)](https://visualgo.net/en/sorting)

- **Tri par tas (Heapsort)** :
    - Fonctionnement : Le tri par tas construit un tas binaire à partir de la liste, puis extrait l'élément maximum (ou
      minimum) à chaque étape pour former une liste triée.
    - Tutoriel vidéo : [Heapsort - Tri par tas (YouTube - Français)](https://www.youtube.com/watch?v=MtQL_ll5KhQ)
    - Pseudocode et explications : [Heap Sort (Programiz)](https://www.programiz.com/dsa/heap-sort)
    - Illustration visuelle : [Heap Sort Visualization (VisuAlgo)](https://visualgo.net/en/sorting)

- **Tri de Shell (Shell Sort)** :
    - Fonctionnement : Le tri de Shell améliore le tri par insertion en comparant et en échangeant des éléments éloignés
      pour réduire progressivement les écarts, jusqu'à ce que la liste soit entièrement triée.
    - Vidéo explicative : [Tri de Shell - Shell Sort (YouTube - Français)](https://www.youtube.com/watch?v=ddeLSDsYVp8)
    - Ressources détaillées : [Shell Sort Explained (GeeksforGeeks)](https://www.geeksforgeeks.org/shellsort/)
    - Démonstration animée : [Shell Sort Animation (VisuAlgo)](https://visualgo.net/en/sorting)
