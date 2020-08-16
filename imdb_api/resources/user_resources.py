from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import user_controller
from validators import validator
from util.encoders import ImdbEncoder

logger = logging.getLogger("imdb_logger")


class RegistrationResource(Resource):
    def post(self):
        """Create the list for a user"""
        logger.debug('/users POST requested')
        data_dict = json.loads(request.data)
        validator.validate(data_dict, validator.USER)

        user = user_controller.register(data_dict)

        response = Response(
            response=json.dumps(user, cls=ImdbEncoder),
            status=201,
            mimetype='application/json'
        )
        return response