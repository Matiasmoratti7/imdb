from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import list_controller
from mappers import list_mapper
from validators import validator

logger = logging.getLogger("imdb_logger")


class ListResource(Resource):
    def get(self):
        """Returns the list of the user"""
        username = request.args.get('username')
        if username is None:
            return "Username parameter missing", 400
        logger.debug(f'/lists GET for user = {username} requested')

        lists = list_controller.get_lists(username)
        if lists is None:
            return "", 404

        lists_dto = list_mapper.get_lists(lists)

        response = Response(
            response=json.dumps(lists_dto),
            status=200,
            mimetype='application/json'
        )
        return response

    def get(self, list_id):
        """Receives a list id and returns the list if available"""
        logger.debug(f'/lists GET by id = {list_id} requested')

        list_object = list_controller.get_list_by_id(list_id)
        if list_object is None:
            return "", 404
        list_dto = list_mapper.get_list(list_object)

        response = Response(
            response=json.dumps(list_dto),
            status=200,
            mimetype='application/json'
        )
        return response

    def post(self):
        """Create the list for a user"""
        logger.debug('/lists POST requested')

        validator.validate_list(request.data)
        data_dict = json.loads(request.data)
        username = data_dict['username']

        list_id = list_controller.create_list(username)

        response = Response(
            response=json.dumps({"list_id": list_id}),
            status=201,
            mimetype='application/json'
        )
        return response


class ListFilmResource(Resource):
    def post(self, list_id, film_id):
        """Add a film to a list"""
        logger.debug(f'/lists/{list_id}/films/{film_id} POST requested')

        list_controller.add_film(list_id, film_id)

        return "", 200


class ListShowResource(Resource):
    def post(self, list_id, show_id):
        """Add a film to a list"""
        logger.debug(f'/lists/{list_id}/films/{show_id} POST requested')

        list_controller.add_show(list_id, show_id)

        return "", 200