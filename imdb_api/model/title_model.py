from entities.title import Title, Film
from sqlalchemy import desc
from config.config import Config


def get_title_by_id(title_id):
    return Title.query.filter_by(id=title_id).first()


def get_titles(args):
    search_params = args
    filters = ["genre", "release_year", "country", "type"]
    sort = search_params.get("sort")
    max = search_params.get("max")

    query = Title.query

    if "release_year" in search_params:
        query = query.filter_by(release_year=search_params.get("release_year"))
        del search_params["release_year"]

    for filter in [a for a in filters if a in search_params]:
        field = getattr(Title, filter)
        filter_clause = field.ilike("%" + search_params.get(filter) + "%")
        query = query.filter(filter_clause)

    if sort:
        if sort == "rating":
            query = query.order_by(desc(Title.rating))
        elif sort == "metascore":
            query = query.join(Film).order_by(desc(Film.metascore))
        elif sort == "release_year":
            query = query.order_by(desc(Title.release_year))

    if not max or max > Config.app.max_titles:
        max = Config.app.default_titles

    return query.limit(max).all()
