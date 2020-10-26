from flask_restful import Resource
import json
from flask import Response, request
from controllers import title_controller
from schemas import title_schema
from validators import validator
from schemas.title_schema import SimplifiedTitleSchema
from entities.title import Title
from flask_filter import query_with_filters

simplified_title_schema = SimplifiedTitleSchema()


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


class TitlesV2Resource(Resource):
    def get(self):
        """Returns a list of titles based on url params
            URL example: imdb/titles?filters=[{'field': 'field_name', 'op': 'operation', 'value': 'field_value'}]
        """
        args = request.args.to_dict()
        validator.validate_title_search_v2(args)

        titles = query_with_filters(Title, args.get("filters"), SimplifiedTitleSchema)

        if not titles:
            return "", 404

        response = Response(
            response=json.dumps(titles), status=200, mimetype="application/json"
        )
        return response

