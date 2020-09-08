from entities.watchlist import Watchlist
from app import db


def get_watchlist_by_user(username):
    return Watchlist.query.filter_by(username=username).first()


def get_watchlist_by_id(watchlist_id):
    return Watchlist.query.filter_by(id=watchlist_id).first()


def create_watchlist(watchlist):
    db.session.add(watchlist)
    db.session.commit()


def add_film(watchlist, film):
    watchlist.films.append(film)
    return watchlist


def add_show(watchlist, show):
    watchlist.shows.append(show)
    return watchlist


def remove_film(watchlist, film):
    watchlist.films.delete(film)
    return watchlist


def remove_show(watchlist, show):
    watchlist.shows.delete(show)
    return watchlist


