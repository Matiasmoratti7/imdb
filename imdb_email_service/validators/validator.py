from cerberus import Validator
from config.logger import get_app_logger

# Schemas

MESSAGE = {
    "subject": {"type": "string", "required": True},
    "body": {"type": "string", "required": True},
    "receiver": {"type": "string", "required": True}
}


def validate(data, schema):
    logger = get_app_logger()
    v = Validator(schema)
    if not v.validate(data):
        logger.critical(f'Malformed message: {v.errors}. Message discarded.')
        return False
    return True
