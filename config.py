import os
from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv()

# Clé API TMDB
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# URL de la base de données
DATABASE_URL = 'sqlite:///films.db'
