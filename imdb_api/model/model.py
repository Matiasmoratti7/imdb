from app import db

"""Importing entities before create_all()"""
from entities.list import List
from entities.user import User, UserTitle
from entities.title import Title, Film, Show, Episode


def initialize_db(app):
    db.init_app(app)
    db.create_all()
