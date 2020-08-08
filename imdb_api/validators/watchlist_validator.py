import json
from exceptions.errors import CustomError
from json.decoder import JSONDecodeError


def validate_watchlist(json_data):
    try:
        dataDict = json.loads(json_data)
    except JSONDecodeError:
            raise CustomError("Wrong format: A JSON Payload is mandatory", 400)

    if 'event_type' not in dataDict:
        raise CustomError("Event {} incomplete, event_type missing".format(dataDict), 400)
    elif 'step_num' not in dataDict:
        raise CustomError("Event {} incomplete, step_num missing".format(dataDict), 400)