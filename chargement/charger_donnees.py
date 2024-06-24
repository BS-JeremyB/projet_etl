from sqlalchemy.orm import sessionmaker
from modeles.film import Film, engine


def charger_donnees(self, films):
    Session = sessionmaker(bind=engine)
    session = Session()

    for film in films:
        film_enregistrement = Film(
            title=film['title'],
            release_date=film['release_date'],
            rating=film['rating'],
            overview=film['overview']
        )
        session.add(film_enregistrement)
    session.commit()
    session.close()


