from model import user_model
from entities.user import User


def get_user_by_username(username):
    return user_model.get_user_by_username(username)


def register(data):
    user = User(data)
    user_model.save(user)
    return user


def login():
    pass