import os

from app import app, db
from model import model


def create(db_string):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TRACKER_DB_CONNECTION_STRING', db_string)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to suppress this parameter's deprecation warnings
    db.app = app
    model.initialize_db(app)

    return app