from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from entities.user import User, UserTitle
from schemas.title_schema import SimplifiedTitleSchema
from app import ma


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User


class UserTitleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserTitle

    title = Nested(SimplifiedTitleSchema)


def serialize_user(user):
    schema = UserSchema()
    return schema.dump(user)


def serialize_user_title(user_title):
    schema = UserTitleSchema()
    return schema.dump(user_title)


def serialize_user_titles(username, user_titles):
    return {
        "user": username,
        "titles": [serialize_user_title(user_title) for user_title in user_titles],
    }
