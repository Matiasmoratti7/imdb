from entities.list import List
from app import db


def get_lists_by_user(user_id):
    return List.query.filter_by(user_id=user_id).all()


def get_list_by_id(list_id):
    return List.query.filter_by(id=list_id).first()


def save(list):
    db.session.add(list)
    db.session.commit()
    return list


def delete_list(list):
    db.session.delete(list)
    db.session.commit()


def add_title(list, title):
    list.titles.append(title)
    db.session.commit()
    return list


def remove_title(list, title):
    list.titles.remove(title)
    db.session.commit()
    return list
