from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import film_controller
from mappers import film_mapper
from validators import validator

logger = logging.getLogger("imdb_logger")


class FilmResource(Resource):
    def get(self, film_id):
        """Receives a film id and returns the film if available"""
        logger.debug(f'/films GET by id = {film_id} requested')

        film = film_controller.get_film_by_id(film_id)
        if film is None:
            return "", 404
        film_dto = film_mapper.get_film(film)

        response = Response(
            response=json.dumps(film_dto),
            status=200,
            mimetype='application/json'
        )
        return response


class FilmsResource(Resource):
    def get(self):
        """Returns a list of films based on url params"""
        validator.validate_content_search(request.args)
        logger.debug(f'/films GET requested. Url params: {request.args}')

        dict_params = json.loads(request.args)
        films = film_controller.get_films(dict_params)
        if films is None:
            return "", 404
        films_dto = film_mapper.get_films(films)

        response = Response(
            response=json.dumps(films_dto),
            status=200,
            mimetype='application/json'
        )
        return response




