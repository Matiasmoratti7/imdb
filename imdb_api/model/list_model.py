from entities.list import List
from app import db


def get_lists_by_user(username):
    return List.query.filter_by(username=username).first()


def get_list_by_id(list_id):
    return List.query.filter_by(id=list_id).first()


def save(list):
    db.session.add(list)
    db.session.commit()
    return list


def delete_list(list):
    db.session.delete(list)
    db.session.commit()


def add_film(list, film):
    list.films.append(film)
    return list


def add_show(list, show):
    list.shows.append(show)
    return list


def remove_film(list, film):
    list.films.delete(film)
    return list


def remove_show(list, show):
    list.shows.delete(show)
    return list


