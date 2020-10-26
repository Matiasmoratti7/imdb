import configparser
import argparse
from ast import literal_eval
import os
from pathlib import Path


class Config(object):

    configs = {}

    @staticmethod
    def load_from_file(config_file):
        config = configparser.ConfigParser()
        folder = Path(os.path.dirname(__file__))
        file_path = folder / config_file
        config.read(file_path)
        Config.configs = {
            key: Config.infer_value_type(value)
            for key, value in config.items("DEFAULT")
        }
        Config.configs = argparse.Namespace(**Config.configs)

    @staticmethod
    def infer_value_type(string):
        try:
            parsed = literal_eval(string)
            return parsed
        except ValueError:
            return string
