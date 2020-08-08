

class Validator(object):

    possible_params = {}
    required_params = {}

    @staticmethod
    def check_existence(params, params_to_validate):
        """
        Check params existence
        :param params: params received
        :param params_to_validate: params which must exist
        :return:
        """
        not_possibles = [param for param in params_to_validate if param not in params]

    def check_possibles(self, params):
        return [param for param in params if param not in self.possible_params]

    def check_required(self, params):
        return [param for param in self.required_params if param not in params]

    def check_values(self, params):
        error_params = {}
        for param in self.possible_params:
            if (param in params) and (params.get(param) not in self.possible_params.get(param)):
                error_params[param] = self.possible_params.get(param)
        return error_params

    def validate(self, params):
        not_possibles = self.check_possibles(params)
        missing_params = self.check_required(params)
        values_error = self.check_values(params)


class FilmValidator(Validator):

    possible_params = {"param1": ["value1", "value2"], "param2": ["value1", "value2"]}
    required_params = {"param1": ["value1", "value2"]}


