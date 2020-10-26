import json
from exceptions.errors import CustomError
from json.decoder import JSONDecodeError
from cerberus import Validator

# Schemas
LIST = {"name": {"type": "string", "required": True}, "public": {"type": "boolean"}}

TITLE_SEARCH = {
    "type": {"type": "string", "allowed": ["show", "film"]},
    "max": {"type": "integer", "min": 1, "max": 250},
    "sort": {"type": "string", "allowed": ["rating", "release_year"]},
    "genre": {"type": "string"},
    "release_year": {"type": "integer"},
    "country": {"type": "string"},
}

FILMS_SEARCH = {
    "type": {"type": "string", "allowed": ["film"], "required": True},
    "max": {"type": "integer", "min": 1, "max": 250},
    "sort": {"type": "string", "allowed": ["rating", "metascore", "release_year"]},
    "genre": {"type": "string"},
    "release_year": {"type": "integer"},
    "country": {"type": "string"},
}


USER = {
    "username": {"type": "string", "required": True},
    "password": {"type": "string", "required": True},
    "fullname": {"type": "string", "required": True},
    "role": {"type": "string", "required": True},
}

LOGIN = {
    "username": {"type": "string", "required": True},
    "password": {"type": "string", "required": True},
}

USER_CONTENT = {
    "criteria": {"type": "string", "allowed": ["watchlist", "rated"], "required": True},
    "type": {"type": "string", "allowed": ["film", "show"]},
}

USER_RATE = {"rate": {"type": "integer", "min": 1, "max": 10, "required": True}}

USER_BUY = {
    "method": {
        "type": "string",
        "required": True,
        "oneof": [
            {
                "allowed": ["credit_card"],
                "excludes": "paypal_account",
                "dependencies": ["cc_number", "cvv", "cc_holder"],
            },
            {
                "allowed": ["paypal"],
                "excludes": ["cc_number", "cvv", "cc_holder"],
                "dependencies": "paypal_account",
            },
        ],
    },
    "paypal_account": {"type": "string"},
    "cc_number": {"type": "integer"},
    "cvv": {"type": "integer", "max": 99999, "min": 100},
    "cc_holder": {"type": "string"},
    "email": {"type": "string", "required": True},
}


def validate(data, schema):
    v = Validator(schema)
    if not v.validate(data):
        raise CustomError(v.errors, 400)


def validate_title_search(data):
    for int_param in ["max", "release_year"]:
        if int_param in data:
            try:
                value = int(data.get(int_param))
            except ValueError:
                raise CustomError(f"{int_param} value must be integer", 400)
            data[int_param] = value

    if "type" in data:
        if data["type"] == "film":
            return validate(data, FILMS_SEARCH)

    return validate(data, TITLE_SEARCH)


def validate_title_search_v2(data):
    pass


def validate_rate(data):
    if "rate" in data:
        try:
            value = int(data.get("rate"))
        except ValueError:
            raise CustomError(f"Rate value must be integer", 400)
        data["rate"] = value

    validate(data, USER_RATE)



