from app import app, create_app
from config.config import Config
from config.logger import configure_logging, get_app_logger
from exceptions.errors import CustomError
import json
from flask import Response, request, redirect
import logging
from flask_restful import Api
from resources.list_resources import ListTitleResource, ListResource
from resources.user_resources import (
    UserResource,
    UserTitlesResource,
    UserLoginResource,
    UserListsResource,
    UserTitleRateResource,
    UserTitleBuyResource,
)
from resources.title_resources import TitlesResource, TitleResource

STAGE = "ini/stage.ini"
PROD = "ini/prod.ini"
TEST = "ini/test.ini"


def run(standalone=False, config_file=STAGE):
    # Storing configs
    Config.load_from_file(config_file)

    # Configure logger
    logger = configure_logging()
    logger.critical("Ready")

    create_app.create(Config.app.db_string, Config.app.jwt_secret_key)

    return flask_app(standalone, Config.app.port)


def flask_app(standalone, port):

    fl_logger = get_app_logger()

    api = Api(app, errors=CustomError)

    # Load resources
    api.add_resource(TitleResource, "/titles/<int:title_id>", endpoint="title_resource")
    api.add_resource(TitlesResource, "/titles")
    api.add_resource(ListResource, "/lists", "/lists/<int:list_id>")
    api.add_resource(ListTitleResource, "/lists/<int:list_id>/titles/<int:title_id>")
    api.add_resource(UserResource, "/users", "/users/<int:user_id>")
    api.add_resource(UserLoginResource, "/users/login")
    api.add_resource(
        UserTitlesResource, "/users/titles", "/users/titles/<int:title_id>"
    )
    api.add_resource(UserTitleRateResource, "/users/titles/<int:title_id>/rate")
    api.add_resource(UserTitleBuyResource, "/users/titles/<int:title_id>/buy")
    api.add_resource(UserListsResource, "/users/lists")

    @app.errorhandler(CustomError)
    def handle_custom_error(error):
        """Catch CustomError exception globally, serialize into JSON, and respond with specified status."""
        payload = dict(error.payload or ())
        payload["status"] = error.status
        payload["message"] = error.message
        response = Response(
            response=json.dumps(payload),
            status=error.status,
            mimetype="application/json",
        )
        return response

    @app.errorhandler(400)
    def handle_bad_request(error):
        raise CustomError(error.description, 400)

    @app.before_request
    def log_request():
        fl_logger.debug(f"{request.path} {request.method} requested")

    fl_logger.critical("Starting imdb_api")
    fl_logger.critical(f"Imdb api listening at port {port}")

    # Run or return the app
    if standalone:
        try:
            app.run(host="0.0.0.0", port=port)
        except (KeyboardInterrupt, EOFError, SystemExit):
            fl_logger.critical("\n\n\t --> Quitting!\n\n")
            quit()
    else:
        return app


if __name__ != "__main__":
    logging.info("imdb_api ready")

if __name__ == "__main__":
    run(standalone=True, config_file=STAGE)
