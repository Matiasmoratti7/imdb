import json
from exceptions.errors import CustomError
from json.decoder import JSONDecodeError


def validate_watchlist(request_data):
    try:
        data_dict = json.loads(request_data)
    except JSONDecodeError:
            raise CustomError("Wrong format: A JSON Payload is mandatory", 400)

    if 'username' not in data_dict:
        raise CustomError("username parameter missing", 400)


def validate_list(request_data):
    try:
        data_dict = json.loads(request_data)
    except JSONDecodeError:
            raise CustomError("Wrong format: A JSON Payload is mandatory", 400)

    if 'username' not in data_dict:
        raise CustomError("username parameter missing", 400)
    if 'name' not in data_dict:
        raise CustomError("name parameter missing", 400)


def validate_content_search(request_data):
    try:
        data_dict = json.loads(request_data)
    except JSONDecodeError:
            raise CustomError("Wrong format: A JSON Payload is mandatory", 400)

    if 'max' in data_dict:
        try:
            max_films = int(data_dict.get('max'))
        except ValueError:
            raise CustomError("Max parameter must be a number", 400)
        if max_films > 250:
            raise CustomError("The max amount of films to be retrieved is 250", 400)

    if 'sort' in data_dict:
        if data_dict.get('sort') not in ["rating", "metascore", "release_date"]:
            raise CustomError("Possible values for sorting are: rating, metascore and release_date", 400)

    if 'filter' in data_dict:
        if data_dict.get('filter') not in ["genre", "release_year", "country"]:
            raise CustomError("Possible values for sorting are: genre, release_year and country", 400)