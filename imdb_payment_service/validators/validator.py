import json
from exceptions.errors import CustomError
from json.decoder import JSONDecodeError
from cerberus import Validator

# Schemas

PAYMENT_DATA = {
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
    "total_amount": {"type": "float", "required": True},
}


def validate(data, schema):
    v = Validator(schema)
    if not v.validate(data):
        raise CustomError(v.errors, 400)

