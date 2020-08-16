from entities.film import Film


def get_film_by_id(film_id):
    return Film.query.filter_by(id=film_id).first()


def get_films(args):
    filters = args.get('filter')
    sort = args.get('sort')
    max = args.get('max')
    query = Film.query

    if filters:
        query = Film.query
        if 'genre' in filters:
            genre_filter = Film.genres.ilike('%' + args.get('genre', "") + '%')
            query = query.filter(genre_filter)
        if 'release_year' in filters:
            year_filter = Film.release_date.ilike('%' + args.get('release_year', "") + '%')
            query = query.filter(year_filter)
        if 'country' in filters:
            country_filter = Film.country == args.get('country')
            query = query.filter(country_filter)

    if sort:
        if sort == 'rating':
            query = query.order_by(Film.user_rating)
        elif sort == 'metascore':
            query = query.order_by(Film.metascore)
        elif sort == 'release_date':
            query = query.order_by(Film.release_date)

    if not max or max > 250:
        max = 10

    return query.limit(max).all()
