from exceptions.errors import CustomError


def check_params(params, required=None, possible=None):
    required = required or {}
    possible = possible or {}
    required_missing = []
    not_possibles = []

    for possible_param in params:
        if possible_param not in possible:
            not_possibles.append(possible_param)

    for required_param in required:
        if required_param not in params:
            required_missing.append(required_param)

    invalid_value_params = check_values(params, possible or required)

    if not_possibles or required_missing or invalid_value_params:
        error_message = "Params error. "
        if not_possibles:
            error_message += " Invalid parameters: "
            for param in not_possibles:
                error_message += param + " "
        if required_missing:
            error_message += " Missing parameters: "
            for param in required_missing:
                error_message += param + " "
        if invalid_value_params:
            for param in invalid_value_params:
                error_message += f'Possible values for {param} are: '
                for value in invalid_value_params.get(param):
                    error_message += value + " "
        raise CustomError(message=error_message, status=400)


def check_values(params, params_validator):
    """
    Check if the params have enabled values
    :param params: dict with the params sent by the client
    :param params_validator: dict with the possible params and its values
    :return: None if correct. A dict the invalid params
    """
    error_params = {}
    for param in params_validator:
        if (param in params) and (params.get(param) not in params_validator.get(param)):
            error_params[param] = params_validator.get(param)

    return error_params or None