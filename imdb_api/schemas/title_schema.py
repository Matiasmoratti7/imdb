from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema, auto_field
from entities.title import Title, Film, Show, Episode
from marshmallow_sqlalchemy import fields
from app import ma
from marshmallow import fields


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film


class EpisodeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Episode

    show_id = auto_field()


class ShowSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Show

    episodes = fields.List(fields.Nested(EpisodeSchema))


def serialize_title(title):
    if isinstance(title, Film):
        schema = FilmSchema()
    elif isinstance(title, Show):
        schema = ShowSchema()
    else:
        schema = EpisodeSchema()
    return schema.dump(title)


def serialize_titles(titles):
    return [serialize_title(title) for title in titles]


class SimplifiedTitleSchema(ma.Schema):
    name = fields.Str()
    type = fields.Str()
    description = fields.Str()
    rating = fields.Float()
    genres = fields.Str()
    title = ma.Hyperlinks(ma.URLFor("title_resource", title_id="<id>"))
