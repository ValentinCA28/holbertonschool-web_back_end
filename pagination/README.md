# Pagination

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![API](https://img.shields.io/badge/Concept-REST%20API-009688.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Implémentation de techniques de pagination pour les API REST : pagination simple, hypermedia et pagination résiliente.

---

## Objectifs d'apprentissage

- Paginer un dataset avec des paramètres `page` et `page_size`
- Implémenter une pagination hypermedia (HATEOAS) avec métadonnées
- Gérer la pagination résiliente face à la suppression de données
- Calculer les index de début et de fin pour une page donnée

---

## Tâches

### 0. Simple helper function
> **Objectif** : Calculer les index de début et de fin pour une page donnée

```python
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retourne (start, end) pour la page demandée."""
    # index_range(1, 7) → (0, 7)
    # index_range(3, 15) → (30, 45)
```

### 1. Simple pagination
> **Objectif** : Paginer un dataset CSV avec validation des paramètres

```python
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retourne la page demandée du dataset."""
        # assert page > 0 et page_size > 0 (integers)
```

### 2. Hypermedia pagination
> **Objectif** : Ajouter des métadonnées hypermedia (HATEOAS) à la pagination

```python
from typing import Dict

class Server:
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retourne un dict avec page_size, page, data, next_page, prev_page, total_pages."""
        # {'page_size': 2, 'page': 1, 'data': [...],
        #  'next_page': 2, 'prev_page': None, 'total_pages': 9709}
```

### 3. Deletion-resilient hypermedia pagination
> **Objectif** : Paginer un dataset indexé par position, résistant à la suppression de lignes

```python
from typing import Dict, List

class Server:
    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexé par position (clé = index original)."""

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Pagination par index : si des lignes sont supprimées entre deux requêtes,
        l'utilisateur ne rate aucun élément."""
        # {'index': 0, 'next_index': 10, 'page_size': 10, 'data': [...]}
```

---

## Dataset

Le fichier `Popular_Baby_Names.csv` contient ~19 000 lignes de prénoms populaires (source : NYC Open Data).

---

## Utilisation

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
```

---

## Requirements

- **Python** 3.12.x
- Style : `pycodestyle` 2.5+
- Tous les fichiers documentés et exécutables

---

[Retour au projet principal](../)
