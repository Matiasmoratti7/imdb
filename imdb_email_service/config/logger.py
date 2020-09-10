import logging
from config.config import Config


def configure_logging():
    """
    Configures logging
    :return: configured logger
    """
    # Create logger
    logger = logging.getLogger("email_logger")
    logger.propagate = False
    logger.setLevel(level=Config.configs.log_level)

    # Create handlers
    ch = logging.StreamHandler()
    if Config.configs.log_file is not None:
        fh = logging.FileHandler(filename=Config.configs.log_file)

    # Format output
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)-8s - %(name)s - %(message)s"
    )
    ch.setFormatter(formatter)
    if Config.configs.log_file is not None:
        fh.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(ch)
    if Config.configs.log_file is not None:
        logger.addHandler(fh)
    return logger


def get_app_logger():
    return logging.getLogger("email_logger")
