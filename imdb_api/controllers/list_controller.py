from model import list_model
from entities.list import List
from datetime import date
from controllers import user_controller


def get_lists_by_user(username):
    return list_model.get_lists_by_user(username)


def get_list_by_id(list_id):
    return list_model.get_list_by_id(list_id)


def create_list(data):
    today = date.today()
    data['creation_date'] = str(today)
    data['user'] = user_controller.get_user_by_username(data.get('username'))
    list_object = List(data)
    list_model.save(list_object)
    return list_object


def delete_list(list):
    list_model.delete_list(list)


def add_film(list, film):
    return list_model.add_film(list, film)


def add_show(list, show):
    pass


def remove_film(list, film):
    pass


def remove_show(list, show):
    pass