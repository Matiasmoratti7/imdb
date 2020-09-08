import json
from exceptions.errors import CustomError
from json.decoder import JSONDecodeError
from cerberus import Validator

# Schemas
LIST = {'username': {'type': 'string', 'required': True},
        'name': {'type': 'string', 'required': True}}

CONTENT_SEARCH = {'max': {'type': 'integer', 'min': 1, 'max': 250},
                  'sort': {'type': 'string', 'allowed': ['rating', 'metascore', 'release_date']},
                  'filter': {'type': 'string', 'allowed': ['genre', 'release_year', 'country']}}

USER = {'username': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True},
        'fullname': {'type': 'string', 'required': True}}


def validate(data, schema):
    v = Validator(schema)
    if not v.validate(data):
        raise CustomError(v.errors, 400)


def validate_content(data):
    if 'max' in data:
        try:
            max = int(data.get('max'))
        except ValueError:
            raise CustomError('Max value must be integer', 400)
        data['max'] = max
    validate(data, CONTENT_SEARCH)