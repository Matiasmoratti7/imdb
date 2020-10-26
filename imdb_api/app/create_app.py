import os

from app import app, db, ma
from model import model
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


def create(db_string, jwt_key):
    # Initialize DB
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "TRACKER_DB_CONNECTION_STRING", db_string
    )
    app.config[
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    ] = False  # to suppress this parameter's deprecation warnings
    db.app = app
    model.initialize_db(app)

    # Initialize Bcrypt and JWTManager for session management
    app.config["JWT_SECRET_KEY"] = jwt_key
    Bcrypt(app)
    JWTManager(app)

    app.config["JSON_SORT_KEYS"] = False

    return app
