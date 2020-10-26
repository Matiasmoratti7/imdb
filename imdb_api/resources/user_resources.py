from flask_restful import Resource
import logging
import json
from flask import Response, request
from controllers import user_controller, title_controller, list_controller
from validators import validator
from schemas import user_schema, list_schema
from exceptions.errors import CustomError
from flask_jwt_extended import jwt_required, get_jwt_identity


class UserResource(Resource):
    def post(self):
        """Register a new user"""
        data_dict = json.loads(request.data)
        validator.validate(data_dict, validator.USER)

        user = user_controller.register(data_dict)
        user_dto = user_schema.serialize_user(user)

        response = Response(
            response=json.dumps(user_dto), status=201, mimetype="application/json"
        )
        return response

    def get(self, user_id):
        """Get a user"""
        user = user_controller.get_user_by_id(user_id)
        if not user:
            return "", 404
        user_dto = user_schema.serialize_user(user)

        response = Response(
            response=json.dumps(user_dto), status=200, mimetype="application/json"
        )
        return response


class UserLoginResource(Resource):
    def post(self):
        """User login"""
        data_dict = json.loads(request.data)
        validator.validate(data_dict, validator.LOGIN)

        token = user_controller.login(data_dict)

        response = Response(
            response=json.dumps({"token": token}),
            status=200,
            mimetype="application/json",
        )
        return response


class UserTitlesResource(Resource):
    @jwt_required
    def get(self):
        """Get user related titles"""
        args = request.args.to_dict()
        validator.validate(args, validator.USER_CONTENT)

        username = get_jwt_identity()

        user_titles = user_controller.get_user_titles(username, args)
        if not user_titles:
            return "", 404
        user_titles_dto = user_schema.serialize_user_titles(username, user_titles)

        response = Response(
            response=json.dumps(user_titles_dto),
            status=200,
            mimetype="application/json",
        )
        return response

    @jwt_required
    def post(self, title_id):
        """Add a title to user's watchlist"""
        username = get_jwt_identity()

        title = title_controller.get_title_by_id(title_id)
        if not title:
            raise CustomError(f"Title {title_id} does not exist")

        user_titles = user_controller.add_title(username, title)
        user_titles_dto = user_schema.serialize_user_titles(username, user_titles)

        response = Response(
            response=json.dumps(user_titles_dto),
            status=200,
            mimetype="application/json",
        )
        return response

    @jwt_required
    def delete(self, title_id):
        """Remove a title from a watchlist"""
        username = get_jwt_identity()

        title = title_controller.get_title_by_id(title_id)
        if not title:
            raise CustomError(f"Title {title_id} does not exist")

        user_titles = user_controller.remove_title(username, title)
        user_titles_dto = user_schema.serialize_user_titles(username, user_titles)

        response = Response(
            response=json.dumps(user_titles_dto),
            status=200,
            mimetype="application/json",
        )
        return response


class UserTitleRateResource(Resource):
    @jwt_required
    def post(self, title_id):
        """Rate a title"""
        username = get_jwt_identity()

        data_dict = json.loads(request.data)
        validator.validate_rate(data_dict)

        title = title_controller.get_title_by_id(title_id)
        if not title:
            raise CustomError(f"Title {title_id} does not exist")

        user_controller.rate_title(title, username, data_dict.get("rate"))

        return "", 200


class UserTitleBuyResource(Resource):
    @jwt_required
    def post(self, title_id):
        """Buy a title"""
        username = get_jwt_identity()

        data_dict = json.loads(request.data)
        validator.validate(data_dict, validator.USER_BUY)

        title = title_controller.get_title_by_id(title_id)
        if not title:
            raise CustomError(f"Title {title_id} does not exist")

        user_controller.buy_title(title, username, data_dict)

        return "", 200


class UserListsResource(Resource):
    @jwt_required
    def get(self):
        """Retrieves the lists of the user"""
        username = get_jwt_identity()

        lists = list_controller.get_lists_by_user(username)
        if not lists:
            return "", 404

        lists_dto = list_schema.serialize_lists(lists)

        response = Response(
            response=json.dumps(lists_dto), status=200, mimetype="application/json"
        )
        return response
