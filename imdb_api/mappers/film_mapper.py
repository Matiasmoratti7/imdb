def get_film(film):
    return {'id': film.id,
            'name': film.name,
            'description': film.description,
            'release_date': film.release_date,
            'stars': film.stars,
            'genres': film.genres,
            'director': film.director,
            'imdb_rating': film.imdb_rating,
            'metascore': film.metascore,
            'country': film.country}


def get_films(films):
    pass