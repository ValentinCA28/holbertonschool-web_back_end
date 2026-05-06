# Python Async Comprehension

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Async](https://img.shields.io/badge/Concept-Asyncio-purple.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Générateurs asynchrones, compréhensions async et exécution parallèle avec `asyncio.gather`.

---

## Objectifs d'apprentissage

- Écrire un générateur asynchrone avec `async for` et `yield`
- Utiliser les compréhensions asynchrones (`async for ... in`)
- Mesurer le temps d'exécution de tâches parallèles avec `asyncio.gather`
- Comprendre le type `AsyncGenerator` du module `typing`

---

## Tâches

### 0. Async Generator
> **Objectif** : Créer un générateur asynchrone qui `yield` des valeurs avec un délai

```python
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 nombres aléatoires entre 0 et 10, avec 1s de pause entre chaque."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### 1. Async Comprehension
> **Objectif** : Collecter les valeurs d'un générateur async via une compréhension async

```python
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Collecte 10 valeurs du générateur async en une seule ligne."""
    return [x async for x in async_generator()]
```

### 2. Run time for four parallel comprehensions
> **Objectif** : Mesurer le temps d'exécution de tâches async en parallèle

```python
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Exécute 4 async_comprehension en parallèle et mesure le temps."""
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start
```

**Pourquoi ~10 secondes et pas ~40 ?** Chaque `async_comprehension()` prend ~10s (10 yields × 1s). Avec `asyncio.gather`, les 4 s'exécutent **concurremment** : pendant qu'une attend son `sleep(1)`, les autres avancent. Résultat : ~10s au total.

---

## Utilisation

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
```

---

## Requirements

- **Python** 3.12.x
- Module `asyncio` (bibliothèque standard)
- Module `typing` pour `AsyncGenerator`, `List`
- Style : `pycodestyle` 2.5+

---

[Retour au projet principal](../)
