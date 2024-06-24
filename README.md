# Projet ETL avec l'API TMDB et SQLAlchemy

## Introduction
Ce projet démontre comment créer un pipeline ETL (Extract, Transform, Load) en utilisant Python. Il extrait des données de l'API TMDB, transforme les données, et les charge dans une base de données SQLite en utilisant SQLAlchemy.

## Structure
- `config.py`: Fichier de configuration pour les clés API et la connexion à la base de données.
- `main.py`: Script principal pour exécuter le processus ETL.
- `extraction/`: Contient les scripts liés à l'extraction des données.
- `transformation/`: Contient les scripts liés à la transformation des données.
- `chargement/`: Contient les scripts liés au chargement des données dans la base de données.
- `modeles/`: Contient les modèles SQLAlchemy pour la base de données.

## Configuration
1. Installer les bibliothèques requises :
    ```sh
    pip install -r requirements.txt
    ```

2. Créer un fichier `.env` avec votre clé API TMDB :
    ```env
    TMDB_API_KEY=votre_cle_api
    ```

## Utilisation
Exécuter le script principal pour lancer le pipeline ETL :
```sh
python main.py
```
