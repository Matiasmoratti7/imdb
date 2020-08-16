from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import list_controller, film_controller, show_controller, user_controller
from mappers import list_mapper
from validators import validator
from exceptions.errors import CustomError
from util.encoders import ImdbEncoder

logger = logging.getLogger("imdb_logger")


class ListResource(Resource):
    def get(self):
        """Returns the list of the user"""
        username = request.args.get('username')
        if username is None:
            return "Username parameter missing", 400
        logger.debug(f'/lists GET for user = {username} requested')

        lists = list_controller.get_lists_by_user(username)
        if not lists:
            return "", 404

        response = Response(
            response=json.dumps(lists, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response

    def get(self, list_id):
        """Receives a list id and returns the list if available"""
        logger.debug(f'/lists GET by id = {list_id} requested')

        list_object = list_controller.get_list_by_id(list_id)
        if not list_object:
            return "", 404

        response = Response(
            response=json.dumps(list_object, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response

    def post(self):
        """Create the list for a user"""
        logger.debug('/lists POST requested')
        data_dict = json.loads(request.data)
        validator.validate(data_dict, validator.LIST)

        username = data_dict['username']
        user = user_controller.get_user_by_username(username)
        if not user:
            raise CustomError("The user specified does not exist", 400)

        list_object = list_controller.create_list(data_dict)

        response = Response(
            response=json.dumps(list_object, cls=ImdbEncoder),
            status=201,
            mimetype='application/json'
        )
        return response

    def delete(self, list_id):
        """Delete a list"""
        logger.debug('/lists DELETE requested')

        list_object = list_controller.get_list_by_id(list_id)

        if not list_object:
            return "", 404

        list_controller.delete_list(list_id)
        return "", 200


class ListFilmResource(Resource):
    def post(self, list_id, film_id):
        """Add a film to a list"""
        logger.debug(f'/lists/{list_id}/films/{film_id} POST requested')

        list_object = list_controller.get_list_by_id(list_id)
        if not list_object:
            raise CustomError(f'List {list_id} does not exist')

        film_object = film_controller.get_film_by_id(film_id)
        if not film_object:
            raise CustomError(f'Film {film_id} does not exist')

        list_object = list_controller.add_film(list_object, film_object)

        response = Response(
            response=json.dumps(list_object, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response

    def delete(self, list_id, film_id):
        """Remove a film from a list"""
        logger.debug(f'/lists/{list_id}/films/{film_id} DELETE requested')

        list_object = list_controller.get_list_by_id(list_id)
        if not list_object:
            raise CustomError(f'List {list_id} does not exist')

        film_object = film_controller.get_film_by_id(film_id)
        if not film_object:
            raise CustomError(f'Film {film_id} does not exist')

        list_object = list_controller.remove_film(list_object, film_object)
        list_dto = list_mapper.get_list(list_object)

        response = Response(
            response=json.dumps(list_dto),
            status=200,
            mimetype='application/json'
        )
        return response


class ListShowResource(Resource):
    def post(self, list_id, show_id):
        """Add a film to a list"""
        logger.debug(f'/lists/{list_id}/films/{show_id} POST requested')

        list_object = list_controller.get_list_by_id(list_id)
        if not list_object:
            raise CustomError(f'List {list_id} does not exist')

        show_object = show_controller.get_show_by_id(show_id)
        if not show_object:
            raise CustomError(f'Show {show_id} does not exist')

        list_object = list_controller.add_show(list_object, show_object)

        response = Response(
            response=json.dumps(list_object, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response

    def delete(self, list_id, show_id):
        """Remove a show from a list"""
        logger.debug(f'/lists/{list_id}/films/{show_id} DELETE requested')

        list_object = list_controller.get_list_by_id(list_id)
        if not list_object:
            raise CustomError(f'List {list_id} does not exist')

        show_object = show_controller.get_show_by_id(show_id)
        if not show_object:
            raise CustomError(f'Show {show_id} does not exist')

        list_object = list_controller.remove_show(list_object, show_object)
        list_dto = list_mapper.get_list(list_object)

        response = Response(
            response=json.dumps(list_dto),
            status=200,
            mimetype='application/json'
        )
        return response