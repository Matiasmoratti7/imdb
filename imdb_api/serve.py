from app import app, create_app
from config.loader import load_from_file
from config.logger import configure_logging, get_app_logger
from exceptions.errors import CustomError
import json
from flask import Response, request, redirect
import logging
from flask_restful import Api
from resources.film_resources import FilmResource, FilmsResource
from resources.show_resources import ShowResource, ShowsResource
from resources.watchlist_resources import WatchlistFilmResource, WatchlistResource, WatchlistShowResource
from resources.list_resources import ListFilmResource, ListResource, ListShowResource
from resources.user_resources import RegistrationResource

STAGE = "/ini/stage.ini"
PROD = "/ini/prod.ini"
TEST = "/ini/test.ini"


def run(standalone=False, config_file=STAGE):
    # Reading arguments
    cl_args = load_from_file(config_file)

    # Configure logger
    logger = configure_logging(cl_args)
    logger.critical("Ready")

    create_app.create(cl_args.db_string)

    return flask_app(standalone, cl_args.port, cl_args.protocol)


def flask_app(standalone, port, protocol):

    fl_logger = get_app_logger()
    app.config['JSON_SORT_KEYS'] = False

    api = Api(app, errors=CustomError)

    # Load resources
    api.add_resource(FilmsResource, '/films')
    api.add_resource(FilmResource, '/films/<int:film_id>')
    api.add_resource(ShowsResource, '/shows')
    api.add_resource(ShowResource, '/shows/<int:show_id>')
    api.add_resource(WatchlistResource, '/watchlists/<int:watchlist_id>', '/watchlists')
    api.add_resource(WatchlistShowResource, '/watchlists/<int:watchlist_id>/shows/<int:show_id>')
    api.add_resource(WatchlistFilmResource, '/watchlists/<int:watchlist_id>/films/<int:film_id>')
    api.add_resource(ListResource, '/lists', '/lists/<int:list_id>')
    api.add_resource(ListShowResource, '/lists/<int:list_id>/shows/<int:show_id>')
    api.add_resource(ListFilmResource, '/lists/<int:list_id>/films/<int:film_id>')
    api.add_resource(RegistrationResource, '/users')

    @app.errorhandler(CustomError)
    def handle_custom_error(error):
        """Catch CustomError exception globally, serialize into JSON, and respond with specified status."""
        payload = dict(error.payload or ())
        payload['status'] = error.status
        payload['message'] = error.message
        response = Response(
            response=json.dumps(payload),
            status=error.status,
            mimetype='application/json'
        )
        return response

    @app.errorhandler(400)
    def handle_bad_request(error):
        raise CustomError(error.description, 400)

    # Redirect functions
    """if protocol == "https":
        @app.before_request
        def redirect_to_ssl():
            criteria = [
                request.is_secure,
                request.headers.get('X-Forwarded-Proto', 'http') == 'https'
            ]

            if not any(criteria):
                if request.url.startswith('http://'):
                    url = request.url.replace('http://', 'https://', 1)
                    code = 302
                    r = redirect(url, code=code)
                    return r"""

    fl_logger.critical("Starting imdb_api")
    fl_logger.critical(f'Imdb api listening at port {port}')

    # Run or return the app
    if standalone:
        try:
            app.run(host='0.0.0.0', port=port)
        except(KeyboardInterrupt, EOFError, SystemExit):
            fl_logger.critical("\n\n\t --> Quitting!\n\n")
            quit()
    else:
        return app


if __name__ != "__main__":
    logging.info("imdb_api ready")

if __name__ == "__main__":
    run(standalone=True, config_file=STAGE)