import configparser
import argparse
from ast import literal_eval


def load_from_file(file):
    config = configparser.ConfigParser()
    config.read(file)
    args = {key: infer_value_type(value) for key, value in config.items("DEFAULT")}
    cl_args = argparse.Namespace(**args)
    return cl_args


def infer_value_type(string):
    try:
        parsed = literal_eval(string)
        return parsed
    except ValueError:
        return string