from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import film_controller
from validators import validator
from util.encoders import ImdbEncoder

logger = logging.getLogger("imdb_logger")


class FilmResource(Resource):
    def get(self, film_id):
        """Receives a film id and returns the film if available"""
        logger.debug(f'/films GET by id = {film_id} requested')

        film = film_controller.get_film_by_id(film_id)
        if not film:
            return "", 404

        response = Response(
            response=json.dumps(film, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response


class FilmsResource(Resource):
    def get(self):
        """Returns a list of films based on url params"""
        args = request.args.to_dict()
        validator.validate_content(args)
        logger.debug(f'/films GET requested. Url params: {args}')

        films = film_controller.get_films(args)
        if not films:
            return "", 404

        response = Response(
            response=json.dumps(films, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response




