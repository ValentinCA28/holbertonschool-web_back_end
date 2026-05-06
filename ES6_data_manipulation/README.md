# ES6 Data Manipulation

![JavaScript](https://img.shields.io/badge/Language-JavaScript-F7DF1E.svg?logo=javascript&logoColor=black)
![ES6](https://img.shields.io/badge/Standard-ES6+-blue.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Manipulation de données avec les structures ES6 : `map`, `filter`, `reduce`, `Set`, `Map`, `WeakMap` et `TypedArray`.

---

## Objectifs d'apprentissage

- Utiliser `map`, `filter` et `reduce` sur des tableaux
- Comprendre et utiliser les `TypedArray` (ArrayBuffer, DataView)
- Manipuler les structures `Set`, `Map` et `WeakMap`
- Combiner plusieurs méthodes de manipulation de données
- Gérer les cas limites (entrées invalides, doublons)

---

## Tâches

### 0. Basic list of objects
> **Objectif** : Créer et retourner un tableau d'objets structurés

```js
export default getListStudents()
// Retourne [{id: 1, firstName: 'Guillaume', location: 'San Francisco'}, ...]
```

### 1. More mapping
> **Objectif** : Extraire un champ spécifique avec `Array.map()`

```js
import getListStudents from './0-get_list_students.js';
export default getListStudentIds(students)
// students.map((student) => student.id) → [1, 2, 5]
```

### 2. Filter
> **Objectif** : Filtrer un tableau d'objets par critère avec `Array.filter()`

```js
export default getStudentsByLocation(students, city)
// students.filter((student) => student.location === city)
```

### 3. Reduce
> **Objectif** : Agréger des valeurs avec `Array.reduce()`

```js
export default getStudentIdsSum(students)
// students.reduce((acc, student) => acc + student.id, 0) → 8
```

### 4. Combine
> **Objectif** : Chaîner `filter` + `map` pour transformer un sous-ensemble de données

```js
export default updateStudentGradeByCity(students, city, newGrades)
// Filtre par ville, puis mappe les notes (grade ou 'N/A' si absente)
```

### 5. Typed Arrays
> **Objectif** : Créer un `ArrayBuffer` et y écrire une valeur `Int8` via `DataView`

```js
export default createInt8TypedArray(length, position, value)
// new ArrayBuffer(length) → DataView → setInt8(position, value)
// Throw Error si position hors limites
```

### 6. Set data structure
> **Objectif** : Créer un `Set` à partir d'un tableau (élimine les doublons)

```js
export default setFromArray(array)
// return new Set(array)
```

### 7. More set data structure
> **Objectif** : Vérifier si tous les éléments d'un tableau existent dans un `Set`

```js
export default hasValuesFromArray(set, array)
// array.every((x) => set.has(x))
```

### 8. Clean set
> **Objectif** : Filtrer les valeurs d'un `Set` par préfixe et formater le résultat

```js
export default cleanSet(set, startString)
// Set(['bonjovi', 'bonaparte'], 'bon') → "jovi-aparte"
```

### 9. Map data structure
> **Objectif** : Créer une `Map` avec des paires clé-valeur

```js
export default groceriesList()
// new Map().set('Apples', 10).set('Tomatoes', 10).set('Pasta', 1)...
```

### 10. More map data structure
> **Objectif** : Itérer et modifier les entrées d'une `Map` conditionnellement

```js
export default updateUniqueItems(map)
// Pour chaque entrée avec value === 1, la remplace par 100
// Throw Error si l'argument n'est pas une Map
```

---

## Utilisation

```bash
npm install
npm run dev 0-main.js
npm test
```

---

## Technologies

- **Node.js** 20.x
- **Babel** 7.x (preset-env)
- **ESLint** (Airbnb base)
- **Jest** pour les tests

---

[Retour au projet principal](../)
