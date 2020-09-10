from app import app
from config.config import Config
from config.logger import configure_logging, get_app_logger
from exceptions.errors import CustomError
import json
from flask import Response, request, redirect
import logging

STAGE = "ini/stage.ini"
PROD = "ini/prod.ini"
TEST = "ini/test.ini"


def run(standalone=False, config_file=STAGE):
    # Storing configs
    Config.load_from_file(config_file)

    # Configure logger
    logger = configure_logging()
    logger.critical("Ready")

    return flask_app(standalone, Config.app.port)


def flask_app(standalone, port):

    fl_logger = get_app_logger()

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

    fl_logger.critical("Starting imdb_payment_service")
    fl_logger.critical(f"Imdb payment service listening at port {port}")

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
    logging.info("imdb_payment_service ready")

if __name__ == "__main__":
    run(standalone=True, config_file=STAGE)
