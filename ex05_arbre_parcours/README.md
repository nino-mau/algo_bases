# 05 – Algorithmes de parcours d'arbre
Compléter `src/parcours.py`, puis `pytest -q ex05_arbre_parcours`.

### Algorithmes présents dans `src/exercices`

Voici une description de chaque algorithme inclus dans ce répertoire. Chaque description comprend une explication du
fonctionnement de l’algorithme ainsi que des ressources pour faciliter l’apprentissage.

#### 1. **Parcours en profondeur (DFS - Depth First Search)**

- **Explication** :
  Le parcours en profondeur visite un nœud, puis explore aussi loin que possible sur chacun de ses voisins avant de
  revenir en arrière. Cela peut être implémenté en utilisant une pile (stack) ou une récursion. L'objectif est de
  parcourir systématiquement tous les chemins possibles pour atteindre un certain point, voire explorer la totalité de
  l’arbre/graphes.
- **Applications** :
    - Résoudre des puzzles (ex. labyrinthes)
    - Recherche de chemins dans un graphe
- **Ressources** :
    - [Visualisation du DFS (vidéo YouTube)](https://youtu.be/oLONftTvpHI)
    - [Explication détaillée sur GeeksForGeeks](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

#### 2. **Parcours en largeur (BFS - Breadth First Search)**

- **Explication** :
  Le parcours en largeur explore un nœud, puis tous ses voisins directs avant de passer à leurs voisins. Cela peut être
  implémenté en utilisant une file (queue). Contrairement au DFS, le BFS explore un par un chaque niveau d’un
  graphe/arbre avant de descendre plus profondément.
- **Applications** :
    - Trouver le chemin le plus court dans un graphe non pondéré
    - Recommandations sociales basées sur la proximité (par exemple, amis communs)
- **Ressources** :
    - [Animation et explication du BFS (vidéo YouTube)](https://youtu.be/UuEJM8YXU7Y)
    - [Documentation sur BFS sur Programiz](https://www.programiz.com/dsa/graph-bfs)

#### 3. **Parcours en ordre (In-order Traversal)**

- **Explication** :
  Dans un parcours in-order, les nœuds d’un arbre binaire sont visités dans l’ordre suivant : sous-arbre gauche, racine,
  sous-arbre droit. Cela convient particulièrement aux arbres de recherche binaire (BST) où les valeurs sont renvoyées
  dans l’ordre croissant.
- **Applications** :
    - Extraction triée d’un arbre de recherche binaire
    - Conversion en collection triée ou traitement séquentiel
- **Ressources** :
    - [Basics and Animation of In-order Traversal (video)](https://youtu.be/G_38iNg0R44)
    - [Tutoriel Interactif Traversal Tree](https://visualgo.net/en/dfsbfs)

#### 4. **Parcours pré-ordre (Pre-order Traversal)**

- **Explication** :
  Ici, chaque nœud est visité avant ses sous-arbres. L’ordre est : racine, sous-arbre gauche, sous-arbre droit, ce qui
  se fait de manière récursive ou via une pile.
- **Applications** :
    - Copier un arbre
    - Conversion en structure linéaire ordonnée
- **Ressources** :
    - [Pre-order Traversal Visualization](https://youtu.be/VHgiIJp-OkY)
