import configparser
import argparse
from ast import literal_eval
import os
from pathlib import Path


class Config(object):

    app = {}
    endpoints = {}

    @staticmethod
    def load_from_file(config_file):
        config = configparser.ConfigParser()
        folder = Path(os.path.dirname(__file__))
        file_path = folder / config_file
        config.read(file_path)
        Config.app = {
            key: Config.infer_value_type(value)
            for key, value in config.items("DEFAULT")
        }
        Config.endpoints = {
            key: Config.infer_value_type(value)
            for key, value in config.items("ENDPOINTS")
        }
        Config.app = argparse.Namespace(**Config.app)
        Config.endpoints = argparse.Namespace(**Config.endpoints)

    @staticmethod
    def infer_value_type(string):
        try:
            parsed = literal_eval(string)
            return parsed
        except ValueError:
            return string
