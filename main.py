from extraction.recuperer_donnees import recuperer_films_populaires
from transformation.transformer_donnees import transformer_films
from chargement.charger_donnees import charger_donnees

def main():
    # Étape 1 : Extraire les données
    print("Extraction des données de l'API TMDB...")
    films = recuperer_films_populaires()

    # Étape 2 : Transformer les données
    print("Transformation des données...")
    films_transformes = transformer_films(films)

    # Étape 3 : Charger les données dans la base de données
    print("Chargement des données dans la base de données...")
    charger_donnees(films_transformes)

    print("Processus ETL terminé avec succès.")

if __name__ == "__main__":
    main()
