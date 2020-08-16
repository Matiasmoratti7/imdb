from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import show_controller
from validators import validator
from util.encoders import ImdbEncoder

logger = logging.getLogger("imdb_logger")


class ShowResource(Resource):
    def get(self, show_id):
        """Receives a show id and returns the show if available"""
        logger.debug(f'/shows GET by id = {show_id} requested')

        show = show_controller.get_show_by_id(show_id)
        if not show:
            return "", 404

        response = Response(
            response=json.dumps(show, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response


class ShowsResource(Resource):
    def get(self):
        """Returns a list of shows based on url params"""
        args = request.args.to_dict()
        validator.validate_content(args)
        logger.debug(f'/shows GET requested. Url params: {args}')

        shows = show_controller.get_shows(args)
        if not shows:
            return "", 404

        response = Response(
            response=json.dumps(shows, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response




