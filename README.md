# Projet ETL en Python : Consommation de l'API TMDB 🎬

Bienvenue dans ce projet ETL ! L'objectif est d'explorer les concepts d'ETL (Extract, Transform, Load) tout en consommant l'API TMDB. Vous apprendrez à extraire des données sur les films, à les transformer selon vos besoins et à les charger dans une base de données. Ce projet est conçu comme un exercice d'apprentissage complet. 🧑‍💻

---

## Configuration et Prérequis 🛠️

### Environnement requis

1. **Python 3.9 ou ultérieur** : téléchargez-le depuis [python.org](https://www.python.org/downloads/).
2. **Un éditeur de code** : comme Visual Studio Code ou PyCharm.
3. **Base de données SQLite** : inclus avec Python.

### Installation des dépendances

Avant de plonger dans le code, installez les dépendances requises avec :

```bash
pip install requests python-dotenv sqlalchemy
```

Ajoutez votre clé API TMDB dans un fichier `.env` :

```env
TMDB_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///tmdb.db
```

---

## Énoncé du Projet 📋

### Votre mission, si vous l'acceptez :

Créez un pipeline ETL en suivant ces étapes :

#### **Étape 1 : Extraction** 🕵️‍♂️

L'extraction se fait dans `extraction/recuperer_donnees.py`.

Implémentez la méthode suivante :

1. `def recuperer_films_populaires():`
   - Récupére les films populaires de l'API TMDB.
   - Retourne une liste de dictionnaires de films.


#### **Étape 2 : Transformation** 🛠️

La transformation se fait dans `transformation/transformer_donnees.py`.

Implémentez les méthodes suivantes :

1. `def gerer_valeurs_manquantes(film):`
   - Gère les champs absents ou avec des valeurs nulles.
   - Exemple : remplace les titres absents par "Titre Inconnu" ou la date de sortie par une valeur par défaut.

2. `def normaliser_format_date(film):`
   - Convertit les dates en format ISO standard.

3. `def convertir_types_donnees(film):`
   - Transforme les champs pour s'assurer qu'ils ont les types appropriés (e.g., float pour les notes).

4. `def nettoyer_champs_texte(film):`
   - Supprime les espaces inutiles ou les caractères spéciaux des chaînes de texte.

5. `def uniformiser_majuscule(film):`
   - Transforme les chaînes de caractères pour s'assurer d'une cohérence dans les majuscules/minuscules.

6. `def valider_donnees_numeriques(film):`
   - Vérifie la validité des champs numériques, comme les notes ou le nombre de votes.

7. `def transformer_films(films):`
   - Ordonne toutes les transformations sur une liste de films et retourne les données prêtes pour le chargement.

#### **Étape 3 : Chargement** 📦

Le chargement se fait dans `chargement/charger_donnees.py` et utilise l'ORM SQLAlchemy.

SQLAlchemy est une bibliothèque permettant d'interagir avec une base de données relationnelle en utilisant des objets Python. Il facilite la gestion des requêtes et des transactions.

Implémentez la méthode suivante :

1. `def charger_donnees(films):`
   - Charge les films dans une base SQLite en utilisant le modèle SQLAlchemy `Film`.
   - Crée une session, ajoute les films un par un, et valide les changements avec un `commit()`.

---

## Structure du Projet 📂

```
projet_etl/
├── extraction/
│   ├── __init__.py
│   ├── recuperer_donnees.py  # Extraction des films depuis TMDB
├── transformation/
│   ├── __init__.py
│   ├── transformer_donnees.py  # Nettoyage et normalisation
├── chargement/
│   ├── __init__.py
│   ├── charger_donnees.py  # Chargement dans SQLite
├── modeles/
│   ├── __init__.py
│   ├── film.py  # Modèle SQLAlchemy
├── config.py  # Configuration des variables globales
├── main.py  # Orchestration ETL
├── requirements.txt
└── .env
```

---

