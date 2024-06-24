import requests
from config import TMDB_API_KEY

def recuperer_films_populaires():
    """
    Récupérer les films populaires de l'API TMDB.
    Retourne une liste de dictionnaires de films.
    """
    URL_DE_BASE = 'https://api.themoviedb.org/3'
    url = f'{URL_DE_BASE}/movie/popular?api_key={TMDB_API_KEY}'
    response = requests.get(url)
    return response.json().get('results', [])
