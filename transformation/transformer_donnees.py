from datetime import datetime
import re

def gerer_valeurs_manquantes(film):
    film['title'] = film.get('title', 'Titre Inconnu')
    film['release_date'] = film.get('release_date', '1900-01-01')
    film['rating'] = film.get('vote_average', 0.0)
    film['overview'] = film.get('overview', 'Pas de résumé disponible')
    return film

def normaliser_format_date(film):
    try:
        film['release_date'] = datetime.strptime(film['release_date'], '%Y-%m-%d').date()
    except ValueError:
        film['release_date'] = datetime(1900, 1, 1).date()
    return film

def convertir_types_donnees(film):
    film['rating'] = float(film['rating'])
    return film

def nettoyer_champs_texte(film):
    film['title'] = re.sub(r'[^a-zA-Z0-9\s]', '', film['title'])
    film['overview'] = re.sub(r'[^a-zA-Z0-9\s]', '', film['overview'])
    return film

def uniformiser_majuscule(film):
    film['title'] = film['title'].title()
    film['overview'] = film['overview'].capitalize()
    return film

def valider_donnees_numeriques(film):
    if not (0 <= film['rating'] <= 10):
        film['rating'] = 0.0
    return film

def transformer_films(films):
    """
    Appliquer une série de transformations à la liste de films.
    """
    transformations = [
        gerer_valeurs_manquantes,
        normaliser_format_date,
        convertir_types_donnees,
        nettoyer_champs_texte,
        uniformiser_majuscule,
        valider_donnees_numeriques
    ]
    for transform in transformations:
        films = [transform(film) for film in films]
    return films
