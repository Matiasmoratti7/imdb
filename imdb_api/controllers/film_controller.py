from model import film_model


def get_film_by_id(film_id):
    return film_model.get_film_by_id(film_id)


def get_films(args):
    return film_model.get_films(args)
