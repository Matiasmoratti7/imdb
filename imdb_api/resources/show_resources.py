from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import show_controller
from mappers import show_mapper
from validators import validator

logger = logging.getLogger("imdb_logger")


class ShowResource(Resource):
    def get(self, show_id):
        """Receives a show id and returns the show if available"""
        logger.debug(f'/shows GET by id = {show_id} requested')

        show = show_controller.get_show_by_id(show_id)
        if show is None:
            return "", 404
        show_dto = show_mapper.get_show(show)

        response = Response(
            response=json.dumps(show_dto),
            status=200,
            mimetype='application/json'
        )
        return response


class ShowsResource(Resource):
    def get(self):
        """Returns a list of shows based on url params"""
        validator.validate_content_search(request.args)
        logger.debug(f'/shows GET requested. Url params: {request.args}')

        dict_params = json.loads(request.args)

        shows = show_controller.get_shows(dict_params)
        if shows is None:
            return "", 404
        shows_dto = show_mapper.get_shows(shows)

        response = Response(
            response=json.dumps(shows_dto),
            status=200,
            mimetype='application/json'
        )
        return response




