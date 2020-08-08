from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import watchlist_controller
from mappers import watchlist_mapper
from validators import validator

logger = logging.getLogger("imdb_logger")


class WatchlistResource(Resource):
    def get(self, watchlist_id):
        """Receives a watchlist id and returns the watchlist if available"""
        logger.debug(f'/watchlists GET by id = {watchlist_id} requested')

        watchlist = watchlist_controller.get_watchlist_by_id(watchlist_id)
        if watchlist is None:
            return "", 404
        watchlist_dto = watchlist_mapper.get_watchlist(watchlist)

        response = Response(
            response=json.dumps(watchlist_dto),
            status=200,
            mimetype='application/json'
        )
        return response

    def post(self):
        """Create the watchlist for a user"""
        logger.debug('/watchlists POST requested')

        validator.validate_watchlist(request.data)
        data_dict = json.loads(request.data)
        username = data_dict['username']

        watchlist_id = watchlist_controller.create_watchlist(username)

        response = Response(
            response=json.dumps({"watchlist_id": watchlist_id}),
            status=201,
            mimetype='application/json'
        )
        return response


class WatchlistFilmResource(Resource):
    def post(self, watchlist_id, film_id):
        """Add a film to a watchlist"""
        logger.debug(f'/watchlists/{watchlist_id}/films/{film_id} POST requested')

        watchlist_controller.add_film(watchlist_id, film_id)

        return "", 200


class WatchlistShowResource(Resource):
    def post(self, watchlist_id, show_id):
        """Add a film to a watchlist"""
        logger.debug(f'/watchlists/{watchlist_id}/shows/{show_id} POST requested')

        watchlist_controller.add_show(watchlist_id, show_id)

        return "", 200