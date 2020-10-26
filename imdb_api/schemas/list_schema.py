from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema, auto_field
from entities.list import List
from marshmallow import fields
from schemas.title_schema import SimplifiedTitleSchema


class ListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = List

    titles = fields.List(fields.Nested(SimplifiedTitleSchema))
    user_id = auto_field()


def serialize_list(list, many=False, only=None):
    schema = ListSchema(many=many, only=only)
    return schema.dump(list)


def serialize_lists(lists):
    if len(lists) > 1:
        return serialize_list(
            lists, many=True, only=["id", "name", "creation_date", "public"]
        )
    else:
        return serialize_list(
            lists, many=False, only=["id", "name", "creation_date", "public"]
        )
