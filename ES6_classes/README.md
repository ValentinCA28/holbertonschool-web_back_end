# ES6 Classes

![JavaScript](https://img.shields.io/badge/Language-JavaScript-F7DF1E.svg?logo=javascript&logoColor=black)
![ES6](https://img.shields.io/badge/Standard-ES6+-blue.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Maîtrise des classes ES6 : constructeurs, getters/setters, héritage, méthodes statiques et polymorphisme.

---

## Objectifs d'apprentissage

- Définir une classe avec un constructeur
- Implémenter des getters et setters avec validation
- Utiliser l'héritage avec `extends` et `super`
- Comprendre les classes abstraites et les méthodes à implémenter
- Surcharger `toString()` et les conversions de type
- Résoudre les problèmes de hoisting avec les classes

---

## Tâches

### 0. ClassRoom
> **Objectif** : Créer une classe simple avec un attribut privé

```js
export default class ClassRoom {
  constructor(maxStudentsSize)  // stocke dans this._maxStudentsSize
}
```

### 1. Make Classrooms
> **Objectif** : Instancier plusieurs objets d'une classe et les retourner dans un tableau

```js
import ClassRoom from './0-classroom.js';
export default function initializeRooms()
// Retourne [ClassRoom(19), ClassRoom(20), ClassRoom(34)]
```

### 2. HolbertonCourse
> **Objectif** : Implémenter des getters/setters avec **validation de types** (TypeError si invalide)

```js
export default class HolbertonCourse {
  constructor(name, length, students)  // string, number, array
  get name() / set name(newName)       // TypeError si pas string
  get length() / set length(newLength) // TypeError si pas number
  get students() / set students(newStudents) // TypeError si pas array
}
```

### 3. Currency
> **Objectif** : Créer une classe avec une méthode d'affichage personnalisée

```js
export default class Currency {
  constructor(code, name)
  displayFullCurrency()  // "Dollars ($)"
}
```

### 4. Pricing
> **Objectif** : Composer des classes entre elles et créer une méthode statique

```js
import Currency from './3-currency.js';
export default class Pricing {
  constructor(amount, currency)          // number, Currency instance
  displayFullPrice()                     // "100 Euro (EUR)"
  static convertPrice(amount, conversionRate)
}
```

### 5. Building (Abstract)
> **Objectif** : Simuler une classe abstraite qui **force** les sous-classes à implémenter une méthode

```js
export default class Building {
  constructor(sqft)
  // Si une sous-classe n'implémente pas evacuationWarningMessage() → Error
}
```

### 6. SkyHighBuilding
> **Objectif** : Hériter d'une classe et implémenter la méthode abstraite requise

```js
import Building from './5-building.js';
export default class SkyHighBuilding extends Building {
  constructor(sqft, floors)          // super(sqft)
  evacuationWarningMessage()         // "Evacuate slowly the 60 floors"
}
```

### 7. Airport
> **Objectif** : Surcharger la représentation string d'un objet avec `Symbol.toStringTag`

```js
export default class Airport {
  constructor(name, code)
  get [Symbol.toStringTag]()  // retourne this._code → "[object SFO]"
}
```

### 8. HolbertonClass (Primitive conversion)
> **Objectif** : Implémenter `Symbol.toPrimitive` pour contrôler la conversion en Number et String

```js
export default class HolbertonClass {
  constructor(size, location)
  [Symbol.toPrimitive](hint)  // 'number' → size, 'string' → location
}
```

### 9. Hoisting
> **Objectif** : Corriger un code cassé par un problème de hoisting (déclaration avant utilisation)

```js
export class HolbertonClass { constructor(year, location) }
export class StudentHolberton { constructor(firstName, lastName, holbertonClass) }
// Les classes doivent être déclarées AVANT d'être instanciées
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
