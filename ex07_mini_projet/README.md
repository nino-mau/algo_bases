# Projet guidé – Labyrinthe (Pygame)

Objectif : réaliser un mini-jeu de labyrinthe avec **chargement de données JSON**,
**affichage**, **déplacements**, **score**, et une **IA de résolution (DFS/BFS)**.

## Pré-requis

- Python 3.10+
- `pip install pygame`

## Format des labyrinthes (JSON)

Chaque fichier `.json` contient :

```json
{
  "name": "lab-small",
  "tileSize": 24,
  "legend": {
    "#": "mur",
    " ": "sol",
    "S": "depart",
    "E": "arrivee",
    "*": "point"
  },
  "grid": ["#####", "#S *#", "# # #", "#  E#", "#####"]
}
```

- `grid` : liste de chaînes, toutes de même longueur (**largeur**).
- Caractères : `#` mur, espace sol, `S` départ (unique), `E` arrivée (unique),
  `*` point à collecter.
- `tileSize` : taille en pixels d'une case (proposition par défaut).

## Ressources

Voici quelques ressources utiles pour t'aider dans ce projet :

### Tutoriels Pygame

- [Documentation officielle de Pygame](https://www.pygame.org/docs/) :
  Référence complète pour comprendre et utiliser les fonctionnalités de Pygame.
- [Tutoriel d'introduction à Pygame (en français)](https://openclassrooms.com/fr/courses/4425106-realisez-un-jeu-video-avec-pygame) :
  Guide pas-à-pas pour démarrer avec Pygame.
- [Making Games with Python & Pygame](https://inventwithpython.com/pygame/) :
  Un livre gratuit pour apprendre et créer des jeux.

### Tutoriels sur les algorithmes en Python

- [Introduction aux algorithmes avec Python (en français)](https://openclassrooms.com/fr/courses/4425126-apprenez-les-bases-des-algorithmes-avec-python) :
  Bases des algorithmes et leur implémentation en Python.
- [Understanding BFS and DFS using Python](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) :
  Apprentissage détaillé de BFS et DFS avec des exemples clairs.
- [Graph Traversal Algorithms](https://realpython.com/graphs-python/#graph-traversal) :
  Traversée de graphes et implémentation de DFS/BFS en Python.

## Étapes proposées

1. **Chargement JSON**
   - Ouvrir un fichier depuis `labyrinths/`.
   - Valider la présence d'un seul `S` et d'un seul `E` ; compter `*`.
   - Construire une structure utile (p.ex. dictionnaire avec `width`, `height`,
     `start`, `end`, `walls:set`, `points:set`).

   Exemple en Python :

   ```python
   import json

   def load_labyrinth(file_path):
       with open(file_path, 'r', encoding='utf-8') as f:
           data = json.load(f)

       grid = data["grid"]
       width = len(grid[0])
       height = len(grid)

       start = None
       end = None
       walls = set()
       points = set()

       for y, row in enumerate(grid):
           for x, cell in enumerate(row):
               if cell == "#":
                   walls.add((x, y))
               elif cell == "S":
                   if start is not None:
                       raise ValueError("Multiple start positions (S) found!")
                   start = (x, y)
               elif cell == "E":
                   if end is not None:
                       raise ValueError("Multiple end positions (E) found!")
                   end = (x, y)
               elif cell == "*":
                   points.add((x, y))

       if start is None or end is None:
           raise ValueError("Missing start (S) or end (E) in the labyrinth!")

       return {
           "width": width,
           "height": height,
           "start": start,
           "end": end,
           "walls": walls,
           "points": points,
       }

   # Exemple d'utilisation :
   labyrinth = load_labyrinth("labyrinths/lab-small.json")
   print(labyrinth)
   ```

2. **Affichage (Pygame)**
   - Fenêtre = `(width * tileSize, height * tileSize)`.
   - Utilisation de Pygame :
     - Initialiser Pygame avec `pygame.init()`.
     - Créer une fenêtre via `pygame.display.set_mode((width, height))`.
     - Définir un titre avec `pygame.display.set_caption("Labyrinthe")`.
   - Palette minimale (exemple) :
     - mur `#` : gris foncé (RGB : `(50, 50, 50)`),
       sol : gris clair `(200, 200, 200)`.
     - `S` : bleu `(0, 0, 255)`, `E` : vert `(0, 255, 0)`,
       `*` : or `(255, 215, 0)`.
   - Exemple d'utilisation pour dessiner une case :

     ```python
     # un mur
     pygame.draw.rect(screen, (50, 50, 50), (x, y, tileSize, tileSize))
     # case départ
     pygame.draw.rect(screen, (0, 0, 255), (x, y, tileSize, tileSize))
     ```

   - Dessiner la grille en rectangles. Facultatif : grille fine de debug :
     - Utiliser `pygame.draw.line()` pour dessiner la grille
       (lignes fines entre les cases).
   - Exemple complet pour dessiner une grille à partir du fichier `grid` :

     ```python
     for y, row in enumerate(grid):
         for x, cell in enumerate(row):
             color = (200, 200, 200) if cell == " " else (50, 50, 50)
             if cell == "S":
                 color = (0, 0, 255)
             elif cell == "E":
                 color = (0, 255, 0)
             elif cell == "*":
                 color = (255, 215, 0)
             pygame.draw.rect(screen, color, (x * tileSize, y * tileSize, tileSize, tileSize))
     ```

3. **Déplacements**
   - Joueur commence en `S`.
   - Touches fléchées (ou ZQSD) → tentative de déplacement (dx,dy).
   - Collision : refuser si la prochaine case est un mur `#`.
   - Fin de partie si la case `E` est atteinte **et** tous les `*` collectés
     (ou à toi de définir la règle).

4. **Score & HUD**
   - Score = nombre de `*` ramassés ; voire un **chrono**
     (tick au `pygame.time.get_ticks()`).
   - Afficher score/chrono en haut à gauche (module `pygame.font`).

5. **IA de résolution (DFS/BFS)**
   - Construire un graphe implicite des cases `non-mur`.
   - **BFS** : plus court chemin `S→E` (distance en cases).
   - **DFS** : chemin quelconque ; comparer nb. de nœuds visités / profondeur.
   - Options pratiques :
     - Touche `I` -> activer l'IA (fait avancer automatiquement case par case).
     - Touche `B` -> choisir BFS ; `D` -> DFS.
     - Touche `R` -> reset depuis `S`.

6. **Mesures & comparaison (bonus)**
   - Instrumenter les recherches : nombre de nœuds visités, longueur de chemin,
     temps.
   - Afficher ces stats en overlay pour **BFS vs DFS** et comparer sur
     différents labyrinthes.

## Suggestions de structure de code

- `loader.py` : lecture/validation JSON → structure Python.
- `game.py` : boucle Pygame (événements, update, draw).
- `search.py` : `bfs(grid, start, goal)`, `dfs(grid, start, goal)`
  retournant un chemin et des stats.
- `main.py` : parse args (`--level labyrinths/lab-small.json`) et lance le jeu.

## Jeux de données

Trois labyrinthes progressifs dans `labyrinths/` :

- `lab-small.json` : petit, didactique (chemin unique, quelques points).
- `lab-medium.json` : taille moyenne, plusieurs branches.
- `lab-large.json` : plus grand, dédales, idéal pour comparer DFS/BFS.

Amuse-toi à modifier/ajouter des `*`, fermer/ouvrir des passages,
et mesurer l'impact sur la difficulté.

```

```
