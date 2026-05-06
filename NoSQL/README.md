# NoSQL

![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248.svg?logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Introduction à MongoDB : opérations CRUD en shell, requêtes avancées et intégration Python avec PyMongo.

---

## Objectifs d'apprentissage

- Comprendre les bases de données NoSQL et leurs avantages
- Différencier SQL et NoSQL
- Maîtriser les opérations CRUD avec MongoDB shell
- Utiliser PyMongo pour interagir avec MongoDB depuis Python
- Effectuer des insertions, mises à jour et requêtes complexes

---

## Tâches

### Scripts MongoDB Shell

#### 0. List all databases
> **Objectif** : Afficher toutes les bases de données du serveur

```js
show databases
```

#### 1. Create a database
> **Objectif** : Créer ou sélectionner une base de données

```js
use my_db
```

#### 2. Insert document
> **Objectif** : Insérer un document dans une collection

```js
db.school.insert({ name: "Holberton school" })
```

#### 3. All documents
> **Objectif** : Lister tous les documents d'une collection

```js
db.school.find()
```

#### 4. All matches
> **Objectif** : Filtrer les documents par critère

```js
db.school.find({ name: "Holberton school" })
```

#### 5. Count
> **Objectif** : Compter le nombre de documents dans une collection

```js
db.school.count()
```

#### 6. Update
> **Objectif** : Modifier des documents existants avec `$set` et `multi: true`

```js
db.school.update(
  { name: "Holberton school" },
  { $set: { address: "972 Mission street" } },
  { multi: true }
)
```

#### 7. Delete by match
> **Objectif** : Supprimer tous les documents correspondant à un critère

```js
db.school.deleteMany({ name: "Holberton school" })
```

---

### Scripts Python (PyMongo)

#### 8. List all documents in Python
> **Objectif** : Lister tous les documents d'une collection via PyMongo

```python
def list_all(mongo_collection):
    """Retourne une liste de tous les documents, ou [] si vide."""
    return list(mongo_collection.find())
```

#### 9. Insert a document in Python
> **Objectif** : Insérer un document via `**kwargs` et retourner le `_id`

```python
def insert_school(mongo_collection, **kwargs):
    """Insère un document et retourne son _id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
```

#### 10. Change school topics
> **Objectif** : Mettre à jour un champ de tous les documents correspondant à un critère

```python
def update_topics(mongo_collection, name, topics):
    """Remplace la liste topics de tous les documents avec le name donné."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
```

---

## Utilisation

### MongoDB Shell
```bash
mongo < 0-list_databases
mongo my_db < 2-insert
```

### Python
```bash
pip3 install pymongo
python3 8-main.py
```

---

## Requirements

- **MongoDB** 4.4+
- **Python** 3.12.x
- **PyMongo** 4.x

---

[Retour au projet principal](../)
