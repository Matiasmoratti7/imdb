import json


class ImdbEncoder(json.JSONEncoder):

    def default(self, obj):
        attrs = obj.__dict__
        return {value:attrs[value] for value in attrs if not value.startswith('_')}