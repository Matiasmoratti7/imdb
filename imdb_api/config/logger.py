import logging
import os
from pathlib import Path


def configure_logging(cl_args):
    """
    Configures logging
    :param cl_args: environment values needed to configure logger
    :return: configured logger
    """
    # Create logger
    logger = logging.getLogger("imdb_logger")
    logger.propagate = False
    logger.setLevel(level=cl_args.log_level)

    # Create handlers
    ch = logging.StreamHandler()
    if cl_args.log_file is not None:
        fh = logging.FileHandler(filename=cl_args.log_file)

    # Format output
    formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    if cl_args.log_file is not None:
        fh.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(ch)
    if cl_args.log_file is not None:
        logger.addHandler(fh)
    return logger


def get_app_logger():
    return logging.getLogger("App.Flask")
