# Python Variable Annotations

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Typing](https://img.shields.io/badge/Concept-Type%20Hints-blue.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Annotations de types en Python 3 : type hints pour les variables, fonctions, et types complexes avec le module `typing`.

---

## Objectifs d'apprentissage

- Comprendre les annotations de types en Python 3
- Utiliser les type hints pour les paramètres et valeurs de retour
- Manipuler les types complexes : `List`, `Tuple`, `Union`, `Callable`
- Valider les annotations avec `mypy`
- Appliquer le duck typing avec les annotations

---

## Tâches

### 0. Basic annotations - add
> **Objectif** : Annoter les types des paramètres et de la valeur de retour d'une fonction simple

```python
def add(a: float, b: float) -> float:
    return a + b
```

### 1. Basic annotations - concat
> **Objectif** : Annoter une fonction de concaténation de strings

```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

### 2. Basic annotations - floor
> **Objectif** : Annoter une fonction dont le type de retour diffère du paramètre

```python
import math

def floor(n: float) -> int:
    return math.floor(n)
```

### 3. Basic annotations - to string
> **Objectif** : Annoter une conversion de type (float → str)

```python
def to_str(n: float) -> str:
    return str(n)
```

### 4. Define variables
> **Objectif** : Annoter des variables directement lors de leur déclaration

```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### 5. Complex types - list of floats
> **Objectif** : Utiliser `typing.List` pour annoter une liste typée

```python
from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

### 6. Complex types - mixed list
> **Objectif** : Utiliser `typing.Union` pour accepter plusieurs types dans une liste

```python
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
```

### 7. Complex types - string and int/float to tuple
> **Objectif** : Annoter une fonction retournant un `Tuple` avec des types différents

```python
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
    # to_kv("eggs", 3) → ('eggs', 9.0)
```

---

## Utilisation

```bash
python3 0-main.py
python3 1-main.py

# Vérification des types avec mypy
mypy 0-add.py
```

---

## Requirements

- **Python** 3.12.x
- Style : `pycodestyle` 2.5+
- Tous les fichiers documentés et exécutables

---

[Retour au projet principal](../)
