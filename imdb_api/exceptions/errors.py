from config.logger import get_app_logger


class CustomError(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, message, status=404, payload=None):
        logger = get_app_logger()
        logger.error("Custom Error raised: {}: {} - {} ".format(message, str(status), payload))
        self.message = message
        self.status = status
        self.payload = payload