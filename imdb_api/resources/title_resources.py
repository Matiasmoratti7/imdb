from flask_restful import Resource
import json
from flask import Response, request
from controllers import title_controller
from schemas import title_schema
from validators import validator


class TitleResource(Resource):
    def get(self, title_id):
        """Get a title by id"""
        title = title_controller.get_title_by_id(title_id)
        if not title:
            return "", 404

        title_dto = title_schema.serialize_title(title)

        response = Response(
            response=json.dumps(title_dto), status=200, mimetype="application/json"
        )
        return response


class TitlesResource(Resource):
    def get(self):
        """Returns a list of titles based on url params"""
        args = request.args.to_dict()
        validator.validate_title_search(args)

        titles = title_controller.get_titles(args)
        if not titles:
            return "", 404

        titles_dto = title_schema.serialize_titles(titles)

        response = Response(
            response=json.dumps(titles_dto), status=200, mimetype="application/json"
        )
        return response
