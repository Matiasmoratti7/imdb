from entities.title import Title, Film
from sqlalchemy import desc


def get_title_by_id(title_id):
    return Title.query.filter_by(id=title_id).first()


def get_titles(args):
    filters = ["genre", "release_year", "country", "type"]
    sort = args.get("sort")
    max = args.get("max")

    query = Title.query

    if "release_year" in args:
        query = query.filter_by(release_year=args.get("release_year"))
        del args["release_year"]

    for filter in [a for a in filters if a in args]:
        field = getattr(Title, filter)
        filter_clause = field.ilike("%" + args.get(filter) + "%")
        query = query.filter(filter_clause)

    if sort:
        if sort == "rating":
            query = query.order_by(desc(Title.rating))
        elif sort == "metascore":
            query = query.join(Film).order_by(desc(Film.metascore))
        elif sort == "release_year":
            query = query.order_by(desc(Title.release_year))

    if not max or max > 250:
        max = 10

    return query.limit(max).all()
