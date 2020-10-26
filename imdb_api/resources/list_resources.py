from flask_restful import Resource
import json
from flask import Response, request
from controllers import list_controller, title_controller
from schemas import list_schema
from validators import validator
from exceptions.errors import CustomError
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_optional


class ListResource(Resource):
    @jwt_optional
    def get(self, list_id):
        """Receives a list id and returns the list if available"""
        username = get_jwt_identity()

        list_object = list_controller.get_list_by_id(list_id, username)
        if not list_object:
            return "", 404

        list_dto = list_schema.serialize_list(list_object)

        response = Response(
            response=json.dumps(list_dto), status=200, mimetype="application/json"
        )
        return response

    @jwt_required
    def post(self):
        """Create a list for a user"""
        username = get_jwt_identity()

        data_dict = json.loads(request.data)
        validator.validate(data_dict, validator.LIST)

        data_dict["username"] = username
        list_object = list_controller.create_list(data_dict)
        list_dto = list_schema.serialize_list(list_object)

        response = Response(
            response=json.dumps(list_dto), status=201, mimetype="application/json"
        )
        return response

    @jwt_required
    def delete(self, list_id):
        """Delete a list"""
        username = get_jwt_identity()

        list_object = list_controller.get_list_by_id(list_id, username)

        if not list_object:
            return "", 404

        list_controller.delete_list(list_object, username)
        return "", 200


class ListTitleResource(Resource):
    @jwt_required
    def post(self, list_id, title_id):
        """Add a title to a list"""
        username = get_jwt_identity()

        list_object = list_controller.get_list_by_id(list_id, username)
        if not list_object:
            raise CustomError(f"List {list_id} does not exist")

        title_object = title_controller.get_title_by_id(title_id)
        if not title_object:
            raise CustomError(f"Title {title_id} does not exist")

        list_object = list_controller.add_title(list_object, title_object, username)
        list_dto = list_schema.serialize_list(list_object)

        response = Response(
            response=json.dumps(list_dto), status=200, mimetype="application/json"
        )
        return response

    @jwt_required
    def delete(self, list_id, title_id):
        """Remove a title from a list"""
        username = get_jwt_identity()

        list_object = list_controller.get_list_by_id(list_id, username)
        if not list_object:
            raise CustomError(f"List {list_id} does not exist")

        title_object = title_controller.get_title_by_id(title_id)
        if not title_object:
            raise CustomError(f"Title {title_id} does not exist")

        list_object = list_controller.remove_title(list_object, title_object, username)
        list_dto = list_schema.serialize_list(list_object)

        response = Response(
            response=json.dumps(list_dto), status=200, mimetype="application/json"
        )
        return response
