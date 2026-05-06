# Python Async Function

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Async](https://img.shields.io/badge/Concept-Asyncio-purple.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Introduction à la programmation asynchrone en Python : coroutines, `async`/`await`, concurrence avec `asyncio` et mesure de performance.

---

## Objectifs d'apprentissage

- Comprendre la syntaxe `async` et `await`
- Exécuter un programme asynchrone avec `asyncio`
- Lancer des coroutines concurrentes avec `asyncio.gather`
- Mesurer le temps d'exécution d'opérations asynchrones
- Créer des `asyncio.Task` pour la concurrence

---

## Tâches

### 0. The basics of async
> **Objectif** : Écrire une coroutine qui attend un délai aléatoire et le retourne

```python
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Attend un délai random entre 0 et max_delay secondes."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
```

### 1. Execute multiple coroutines concurrently
> **Objectif** : Lancer n coroutines en parallèle et collecter les résultats au fur et à mesure

```python
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Exécute wait_random n fois en concurrence, retourne les délais dans l'ordre de complétion."""
    # Utilise asyncio.as_completed() pour collecter les résultats au fur et à mesure
```

### 2. Measure the runtime
> **Objectif** : Mesurer le temps total d'exécution et calculer le temps moyen par appel

```python
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Retourne total_time / n (temps moyen par coroutine)."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
```

### 3. Tasks
> **Objectif** : Créer un `asyncio.Task` à partir d'une coroutine (au lieu de l'attendre directement)

```python
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Crée et retourne un asyncio.Task wrappant wait_random."""
    return asyncio.create_task(wait_random(max_delay))
```

### 4. Tasks (version de wait_n)
> **Objectif** : Réécrire `wait_n` en utilisant des Tasks au lieu d'appels directs

```python
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Comme wait_n, mais utilise task_wait_random au lieu de wait_random."""
```

---

## Concept clé : Concurrence vs Parallélisme

```
Séquentiel (3 × 3s) :  |---3s---|---3s---|---3s---| = 9s total
Concurrent (3 × 3s) :  |---3s---|
                        |---3s---|                    = ~3s total
                        |---3s---|
```

`asyncio` est **concurrent** (un seul thread, bascule entre tâches pendant les `await`), pas **parallèle** (multi-thread/multi-process).

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
- Style : `pycodestyle` 2.5+

---

[Retour au projet principal](../)
