# ES6 Data Manipulation — Cours complet

## Sommaire
1. [Les Arrow Functions](#1-les-arrow-functions)
2. [La méthode .map()](#2-la-méthode-map)
3. [La méthode .filter()](#3-la-méthode-filter)
4. [La méthode .reduce()](#4-la-méthode-reduce)
5. [Combiner .filter() et .map()](#5-combiner-filter-et-map)
6. [ArrayBuffer et DataView](#6-arraybuffer-et-dataview)
7. [Set](#7-set)
8. [Map](#8-map)
9. [Méthodes utiles](#9-méthodes-utiles)

---

## 1. Les Arrow Functions

Avant ES6, on écrivait les fonctions comme ça :

```js
function direBonjour() {
    return "Bonjour !";
}
```

Avec ES6, on utilise les **arrow functions** :

```js
const direBonjour = () => {
    return "Bonjour !";
};
```

### Décomposition

| Morceau | Rôle |
|---|---|
| `const direBonjour` | variable qui contient la fonction |
| `=` | on assigne la fonction à la variable |
| `()` | les paramètres (vide ici) |
| `=>` | la "flèche", signifie *"fait ceci"* |
| `{ return ... }` | le corps de la fonction |

### Avec des paramètres

```js
const additionner = (a, b) => {
    return a + b;
};

additionner(2, 3); // 5
```

### Version courte (return implicite)

Si la fonction ne fait qu'une seule opération :

```js
const additionner = (a, b) => a + b;
```

### Export / Import

Pour rendre une fonction disponible dans d'autres fichiers :

```js
// dans mon_fichier.js
const maFonction = () => { ... };
export default maFonction;

// dans un autre fichier
import maFonction from "./mon_fichier.js";
```

---

## 2. La méthode .map()

`.map()` parcourt chaque élément d'un tableau et retourne un **nouveau tableau transformé**.

```js
const nombres = [1, 2, 3];
const doubles = nombres.map((n) => n * 2);
// doubles = [2, 4, 6]
```

> ⚠️ Le tableau original n'est **pas modifié**.

### Avec un tableau d'objets

```js
const students = [
    { id: 1, firstName: 'Guillaume' },
    { id: 2, firstName: 'James' },
];

const ids = students.map((student) => student.id);
// ids = [1, 2]
```

### Exemple complet

```js
const getListStudentIds = (students) => {
    if (!Array.isArray(students)) return [];
    return students.map((student) => student.id);
};
```

---

## 3. La méthode .filter()

`.filter()` garde uniquement les éléments qui respectent une condition.

```js
const nombres = [1, 2, 3, 4, 5];
const pairs = nombres.filter((n) => n % 2 === 0);
// pairs = [2, 4]
```

### Avec un tableau d'objets

```js
const getStudentsByLocation = (students, city) => {
    return students.filter((student) => student.location === city);
};
```

### Différence avec .map()

| Méthode | Rôle |
|---|---|
| `.map()` | **transforme** chaque élément |
| `.filter()` | **garde ou supprime** des éléments |

---

## 4. La méthode .reduce()

`.reduce()` **accumule** tous les éléments en une seule valeur.

```js
const nombres = [1, 2, 3, 4];
const somme = nombres.reduce((acc, n) => acc + n, 0);
// somme = 10
```

### Décomposition

| Morceau | Rôle |
|---|---|
| `acc` | l'**accumulateur** (la valeur qui s'accumule) |
| `n` | l'élément **actuel** du tableau |
| `acc + n` | ce qu'on fait à chaque étape |
| `0` | la **valeur de départ** de `acc` |

### Étape par étape

```
départ  → acc = 0
étape 1 → acc = 0 + 1 = 1
étape 2 → acc = 1 + 2 = 3
étape 3 → acc = 3 + 3 = 6
étape 4 → acc = 6 + 4 = 10
```

### Exemple complet

```js
const getStudentIdsSum = (students) => {
    return students.reduce((acc, student) => acc + student.id, 0);
};
```

---

## 5. Combiner .filter() et .map()

On peut **chaîner** les méthodes : d'abord filtrer, ensuite transformer.

```js
const updateStudentGradeByCity = (students, city, newGrades) => {
    return students
        .filter((student) => student.location === city)
        .map((student) => {
            const gradeObj = newGrades.find((g) => g.studentId === student.id);
            return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
        });
};
```

### Concepts utilisés

**Le spread operator `...`** : copie toutes les propriétés d'un objet

```js
const student = { id: 1, firstName: 'Guillaume' };
const newStudent = { ...student, grade: 86 };
// { id: 1, firstName: 'Guillaume', grade: 86 }
```

**L'opérateur ternaire** : raccourci pour if/else

```js
condition ? valeurSiVrai : valeurSiFaux

// Exemple
gradeObj ? gradeObj.grade : 'N/A'
```

**La méthode `.find()`** : trouve le premier élément qui correspond

```js
const found = newGrades.find((g) => g.studentId === student.id);
// retourne l'objet trouvé ou undefined
```

---

## 6. ArrayBuffer et DataView

### ArrayBuffer

Un `ArrayBuffer` est un **bloc de mémoire brute** (suite d'octets vides) :

```js
const buffer = new ArrayBuffer(10);
// crée 10 octets vides : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### DataView

`ArrayBuffer` seul ne peut pas être lu ou modifié. `DataView` est une interface pour interagir avec le buffer :

```js
const buffer = new ArrayBuffer(10);
const view = new DataView(buffer);

view.setInt8(2, 89); // écrit 89 à la position 2
```

### Exemple complet

```js
const createInt8TypedArray = (length, position, value) => {
    const buffer = new ArrayBuffer(length);
    const view = new DataView(buffer);

    if (position < 0 || position >= length) {
        throw new Error('Position outside range');
    }

    view.setInt8(position, value);
    return view;
};
```

### Lancer une erreur

```js
throw new Error('Message d\'erreur');
```

---

## 7. Set

Un `Set` est comme un tableau mais **sans doublons**.

```js
new Set([1, 2, 2, 3, 3]);
// Set { 1, 2, 3 }
```

### Créer un Set depuis un tableau

```js
const setFromArray = (array) => {
    return new Set(array);
};
```

### Méthodes utiles

```js
const monSet = new Set([1, 2, 3]);

monSet.has(2);   // true  — vérifie si une valeur existe
monSet.has(10);  // false
monSet.add(4);   // ajoute une valeur
monSet.size;     // 4 — nombre d'éléments
```

### Vérifier si tous les éléments d'un tableau existent dans un Set

`.every()` vérifie si **tous** les éléments respectent une condition :

```js
const hasValuesFromArray = (set, array) => {
    return array.every((element) => set.has(element));
};
```

### Convertir un Set en tableau

```js
Array.from(monSet);
// [1, 2, 3]
```

### Exemple avec filter/map/join sur un Set

```js
const cleanSet = (set, startString) => {
    if (!startString || typeof startString !== 'string') return '';
    return Array.from(set)
        .filter((val) => val.startsWith(startString))
        .map((val) => val.slice(startString.length))
        .join('-');
};
```

**Méthodes string utilisées :**

```js
'bonjovi'.startsWith('bon')  // true — commence par 'bon' ?
'bonjovi'.slice(3)           // 'jovi' — coupe les 3 premiers caractères
'bonjovi'.length             // 7 — longueur de la string
['jovi', 'aparte'].join('-') // 'jovi-aparte' — tableau → string
```

---

## 8. Map

Un `Map` stocke des paires **clé → valeur**.

```js
const maMap = new Map();
maMap.set('Apples', 10);
maMap.set('Bananas', 5);
// Map { 'Apples' => 10, 'Bananas' => 5 }
```

### Créer et chaîner les .set()

```js
const groceriesList = () => {
    const map = new Map();
    return map
        .set('Apples', 10)
        .set('Tomatoes', 10)
        .set('Pasta', 1)
        .set('Rice', 1)
        .set('Banana', 5);
};
```

### Parcourir un Map avec .forEach()

```js
map.forEach((value, key) => {
    console.log(key, value);
});
```

### Vérifier le type avec instanceof

```js
map instanceof Map    // true
"hello" instanceof Map // false
```

### Exemple complet

```js
const updateUniqueItems = (map) => {
    if (!(map instanceof Map)) throw new Error('Cannot process');

    map.forEach((value, key) => {
        if (value === 1) map.set(key, 100);
    });

    return map;
};
```

---

## 9. Méthodes utiles

### Vérifier le type d'une variable

```js
Array.isArray([1, 2, 3])     // true  — est-ce un tableau ?
"hello" instanceof Map        // false — est-ce un Map ?
typeof "hello" === 'string'   // true  — quel est le type ?
typeof 42 === 'number'        // true
```

### Récap des méthodes de tableau

| Méthode | Rôle | Retourne |
|---|---|---|
| `.map()` | transforme chaque élément | nouveau tableau |
| `.filter()` | garde les éléments qui passent le test | nouveau tableau |
| `.reduce()` | accumule en une valeur | une valeur |
| `.find()` | trouve le premier élément qui correspond | l'élément ou `undefined` |
| `.every()` | teste si tous les éléments passent le test | booléen |
| `.forEach()` | parcourt sans retourner | `undefined` |

---

*Cours rédigé à partir des exercices ES6_data_manipulation — Holberton School*
