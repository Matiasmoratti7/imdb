import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'test'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'test'


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:converge@localhost:5432/minds_converge"


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    uri = os.getenv('TRACKER_DB_CONNECTION_STRING', "postgres://postgres:converge@localhost:5432/minds_converge")
    SQLALCHEMY_DATABASE_URI = uri


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}