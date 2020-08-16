from app import db
"""Importing entities before create_all()"""
from entities.show import Show
from entities.film import Film
from entities.watchlist import Watchlist
from entities.list import List
from entities.user import User
from entities.episode import Episode


def initialize_db(app):
    db.init_app(app)
    db.create_all()