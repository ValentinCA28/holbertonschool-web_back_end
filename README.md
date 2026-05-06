# Web Back End

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/Language-JavaScript-F7DF1E.svg?logo=javascript&logoColor=black)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248.svg?logo=mongodb&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)

> Projets back-end couvrant ES6, Python avancé, NoSQL et la pagination, réalisés dans le cadre du cursus Holberton School.

---

## Table des matières

- [Description](#-description)
- [Technologies](#-technologies)
- [Structure du projet](#-structure-du-projet)
- [Projets](#-projets)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Auteur](#-auteur)

---

## Description

Ce repository regroupe l'ensemble des projets **back-end** du cursus Holberton School. Il couvre les fondamentaux de JavaScript moderne (ES6+), la programmation asynchrone en Python, les annotations de types, les bases de données NoSQL avec MongoDB, et les techniques de pagination d'API.

---

## Technologies

| Technologie | Version | Utilisation |
|-------------|---------|-------------|
| Python | 3.12.x | Async, annotations, pagination |
| Node.js | 20.x | ES6 modules, classes, data manipulation |
| MongoDB | 4.4+ | Base de données NoSQL |
| Jest | 24+ | Tests unitaires JavaScript |
| Babel | 7.x | Transpilation ES6+ |
| ESLint | 6+ | Linting JavaScript (Airbnb style) |

---

## Structure du projet

```
holbertonschool-web_back_end/
├── ES6_basic/                    # Fondamentaux ES6
├── ES6_classes/                  # Classes et héritage ES6
├── ES6_data_manipulation/        # Map, Set, Filter, Reduce
├── NoSQL/                        # MongoDB - requêtes et scripts Python
├── pagination/                   # Pagination simple et hypermedia
├── python_async_comprehension/   # Générateurs et compréhensions async
├── python_async_function/        # Coroutines et concurrence async
├── python_variable_annotations/  # Type annotations Python
└── README.md
```

---

## Projets

### JavaScript (ES6+)

| Projet | Description | Fichiers |
|--------|-------------|----------|
| [ES6 Basic](./ES6_basic/) | `let`/`const`, arrow functions, spread, rest, template literals, iterators | 13 exercices |
| [ES6 Classes](./ES6_classes/) | Classes, héritage, getters/setters, méthodes statiques, polymorphisme | 10 exercices |
| [ES6 Data Manipulation](./ES6_data_manipulation/) | `map`, `filter`, `reduce`, `Set`, `Map`, `WeakMap`, `TypedArray` | 11 exercices |

### Python

| Projet | Description | Fichiers |
|--------|-------------|----------|
| [Variable Annotations](./python_variable_annotations/) | Type hints, `typing` module, annotations de fonctions et variables | 8 exercices |
| [Async Function](./python_async_function/) | `async`/`await`, coroutines, `asyncio.gather`, mesure de temps | 5 exercices |
| [Async Comprehension](./python_async_comprehension/) | Générateurs async, compréhensions async, exécution parallèle | 3 exercices |
| [Pagination](./pagination/) | Pagination simple, hypermedia, pagination résiliente à la suppression | 4 exercices |

### Base de données

| Projet | Description | Fichiers |
|--------|-------------|----------|
| [NoSQL](./NoSQL/) | MongoDB : CRUD, requêtes, scripts shell et intégration Python (PyMongo) | 11 exercices |

---

## Requirements

### Python
- Python 3.12.x
- Style : `pycodestyle` 2.5+
- Tous les fichiers exécutables avec `#!/usr/bin/env python3`
- Modules et fonctions documentés

### JavaScript
- Node.js 20.x
- Babel 7.x + preset-env
- ESLint (Airbnb base)
- Jest pour les tests

### MongoDB
- MongoDB 4.4+
- PyMongo pour les scripts Python

---

## Installation

### Projets JavaScript
```bash
cd ES6_basic  # ou ES6_classes, ES6_data_manipulation
npm install
npm run dev <fichier>.js
npm test
```

### Projets Python
```bash
cd python_variable_annotations  # ou autre dossier Python
python3 <fichier_main>.py
```

### MongoDB
```bash
cd NoSQL
# Shell MongoDB
mongo < 0-list_databases
# Scripts Python
python3 8-main.py
```

---

## Auteur

- **Valentin Planchon** - [GitHub](https://github.com/ValentinCA28)

---

<div align="center">

**Holberton School - Web Back End**

*Développé avec passion par Valentin Planchon*

[Retour en haut](#web-back-end)

</div>
