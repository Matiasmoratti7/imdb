import configparser
import argparse
from ast import literal_eval
import os
from pathlib import Path


def load_from_file(config_file):
    config = configparser.ConfigParser()
    file_path = Path(os.path.dirname(__file__) + config_file)
    config.read(file_path)
    args = {key: infer_value_type(value) for key, value in config.items("DEFAULT")}
    cl_args = argparse.Namespace(**args)
    return cl_args


def infer_value_type(string):
    try:
        parsed = literal_eval(string)
        return parsed
    except ValueError:
        return string