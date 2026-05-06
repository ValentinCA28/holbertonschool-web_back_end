# ES6 Basic

![JavaScript](https://img.shields.io/badge/Language-JavaScript-F7DF1E.svg?logo=javascript&logoColor=black)
![ES6](https://img.shields.io/badge/Standard-ES6+-blue.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Introduction aux fondamentaux d'ECMAScript 6 : déclarations de variables, arrow functions, paramètres par défaut, spread/rest, et itération.

---

## Objectifs d'apprentissage

- Comprendre la différence entre `var`, `let` et `const`
- Utiliser les arrow functions et leur impact sur `this`
- Maîtriser les paramètres par défaut et le rest parameter
- Utiliser le spread operator pour les tableaux et objets
- Appliquer les template literals et le shorthand property
- Itérer avec `for...of`

---

## Stack technique

| Outil | Version | Rôle | Installation |
|-------|---------|------|-------------|
| ![Node.js](https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white) | 20.x | Runtime JavaScript | [nodejs.org](https://nodejs.org/) |
| ![Babel](https://img.shields.io/badge/Babel-F9DC3E?logo=babel&logoColor=black) | 7.6+ | Transpiler ES6+ → ES5 | `@babel/core` `@babel/node` `@babel/preset-env` |
| ![ESLint](https://img.shields.io/badge/ESLint-4B32C3?logo=eslint&logoColor=white) | 6.8+ | Linter (Airbnb style) | `eslint` `eslint-config-airbnb-base` `eslint-plugin-import` |
| ![Jest](https://img.shields.io/badge/Jest-C21325?logo=jest&logoColor=white) | 24.9+ | Framework de tests | `jest` `eslint-plugin-jest` |

---

## Tâches

### 0. Const or let?
> **Objectif** : Remplacer `var` par `const` et `let` selon le contexte

```js
export function taskFirst()    // utilise const
export function getLast()
export function taskNext()     // utilise let
```

### 1. Block Scope
> **Objectif** : Comprendre la portée de bloc avec `let` et `const` dans les blocs conditionnels

```js
export default function taskBlock(trueOrFalse)
// Les variables déclarées avec const dans un if ne modifient pas celles du scope parent
```

### 2. Arrow Functions
> **Objectif** : Convertir une fonction classique en arrow function pour conserver le contexte `this`

```js
export default function getNeighborhoodsList()
// this.addNeighborhood = (newNeighborhood) => { ... }
```

### 3. Parameter Defaults
> **Objectif** : Utiliser les paramètres par défaut pour simplifier les appels de fonction

```js
export default (initialNumber, expansion1989 = 89, expansion2019 = 19) => ...
```

### 4. Rest Parameter
> **Objectif** : Utiliser le rest parameter `...args` pour gérer un nombre variable d'arguments

```js
export default function returnHowManyArguments(...args)
// Retourne args.length
```

### 5. Spread Operator
> **Objectif** : Utiliser le spread operator `...` pour concaténer tableaux et strings

```js
export default function concatArrays(array1, array2, string)
// return [...array1, ...array2, ...string]
```

### 6. Template Literals
> **Objectif** : Utiliser les template literals `` `${}` `` pour l'interpolation de variables

```js
export default function getSanFranciscoDescription()
// `As of ${year}, it was the seventh-highest...`
```

### 7. Object Property Shorthand
> **Objectif** : Utiliser la syntaxe shorthand pour les propriétés d'objets

```js
export default function getBudgetObject(income, gdp, capita)
// return { income, gdp, capita }  au lieu de { income: income, ... }
```

### 8. Computed Property Names
> **Objectif** : Utiliser les noms de propriétés calculés avec `[]` dans un objet

```js
export default function getBudgetForCurrentYear(income, gdp, capita)
// { [`income-${getCurrentYear()}`]: income, ... }
```

### 9. ES6 Method Properties
> **Objectif** : Utiliser la syntaxe raccourcie pour les méthodes d'objets

```js
import getBudgetObject from './7-getBudgetObject.js';
export default function getFullBudgetObject(income, gdp, capita)
// getIncomeInDollars(income) { ... }  au lieu de getIncomeInDollars: function(income) { ... }
```

### 10. For...of Loops
> **Objectif** : Remplacer `for...in` par `for...of` avec `array.entries()` pour itérer proprement

```js
export default appendToEachArrayValue(array, appendString)
// for (const [idx, value] of array.entries()) { ... }
```

### 11. Iterator
> **Objectif** : Créer dynamiquement un objet avec des computed property names

```js
export default function createEmployeesObject(departmentName, employees)
// return { [departmentName]: employees }
```

### 12. Report Object
> **Objectif** : Créer un objet avec une méthode qui opère sur ses propres propriétés via `this`

```js
export default function createReportObject(employeesList)
// { allEmployees: ..., getNumberOfDepartments() { return Object.keys(this.allEmployees).length } }
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-ES6%20Basic-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
