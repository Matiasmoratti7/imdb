from entities.show import Show


def get_show_by_id(show_id):
    return Show.query.filter_by(id=show_id).first()


def get_shows(args):
    filters = args.get('filter')
    sort = args.get('sort')
    max = args.get('max') or 10
    query = Show.query

    if filters:
        query = Show.query
        if 'genre' in filters:
            genre_filter = Show.genres.ilike('%' + args.get('genre', "") + '%')
            query = query.filter(genre_filter)
        if 'release_year' in filters:
            year_filter = Show.release_date.ilike('%' + args.get('release_year', "") + '%')
            query = query.filter(year_filter)
        if 'country' in filters:
            country_filter = Show.country == args.get('country')
            query = query.filter(country_filter)

    if sort:
        if sort == 'rating':
            query = query.order_by(Show.user_rating)
        elif sort == 'metascore':
            query = query.order_by(Show.metascore)
        elif sort == 'release_date':
            query = query.order_by(Show.release_date)

    query = query.limit(max <= 250 or 10)

    return query.all()
