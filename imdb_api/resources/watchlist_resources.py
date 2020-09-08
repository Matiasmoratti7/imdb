from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import watchlist_controller, film_controller, show_controller
from mappers import watchlist_mapper
from exceptions.errors import CustomError
from util.encoders import ImdbEncoder

logger = logging.getLogger("imdb_logger")


class WatchlistResource(Resource):
    def get(self, watchlist_id):
        """Receives a watchlist id and returns the watchlist if available"""
        logger.debug(f'/watchlists GET by id = {watchlist_id} requested')

        watchlist = watchlist_controller.get_watchlist_by_id(watchlist_id)
        if not watchlist:
            return "", 404

        response = Response(
            response=json.dumps(watchlist, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response


class WatchlistFilmResource(Resource):
    def post(self, watchlist_id, film_id):
        """Add a film to a watchlist"""
        logger.debug(f'/watchlists/{watchlist_id}/films/{film_id} POST requested')

        watchlist = watchlist_controller.get_watchlist_by_id(watchlist_id)
        if not watchlist:
            raise CustomError(f'Watchlist {watchlist_id} does not exist')

        film = film_controller.get_film_by_id(film_id)
        if not film:
            raise CustomError(f'Film {film_id} does not exist')

        watchlist_object = watchlist_controller.add_film(watchlist_id, film_id)

        response = Response(
            response=json.dumps(watchlist_object, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response


class WatchlistShowResource(Resource):
    def post(self, watchlist_id, show_id):
        """Add a film to a watchlist"""
        logger.debug(f'/watchlists/{watchlist_id}/shows/{show_id} POST requested')

        watchlist = watchlist_controller.get_watchlist_by_id(watchlist_id)
        if not watchlist:
            raise CustomError(f'Watchlist {watchlist_id} does not exist')

        show = show_controller.get_show_by_id(show_id)
        if not show:
            raise CustomError(f'Show {show_id} does not exist')

        watchlist_object = watchlist_controller.add_show(watchlist_id, show_id)

        response = Response(
            response=json.dumps(watchlist_object, cls=ImdbEncoder),
            status=200,
            mimetype='application/json'
        )
        return response