from model import list_model
from entities.list import List
from datetime import date
from controllers import user_controller
from exceptions.errors import CustomError


def get_lists_by_user(username):
    user = user_controller.get_user_by_username(username)
    return list_model.get_lists_by_user(user.id)


def create_list(data):
    data["user"] = user_controller.get_user_by_username(data.get("username"))
    list_object = List(data)
    list_model.save(list_object)
    return list_object


def check_list_access(func):
    def validate(*args):
        list = args[0]
        username = args[2]
        if not (
            list.public
            or user_controller.is_admin(username)
            or list.user.username == username
        ):
            raise CustomError("The user can't operate this list", 401)
        return func(*args)

    return validate


def get_list_by_id(list_id, username):
    list = list_model.get_list_by_id(list_id)
    if not list:
        return None
    if list.public or (
        username
        and (user_controller.is_admin(username) or list.user.username == username)
    ):
        return list_model.get_list_by_id(list_id)
    raise CustomError("The user can't operate this list", 401)


@check_list_access
def add_title(list, title, username):
    if list.title_exists(title):
        raise CustomError("The title is already on the list", 400)
    return list_model.add_title(list, title)


def delete_list(list, username):
    if user_controller.is_admin(username) or list.user.username == username:
        return list_model.delete_list(list)
    raise CustomError("The user can't operate this list", 401)


@check_list_access
def remove_title(list, title, username):
    return list_model.remove_title(list, title)
