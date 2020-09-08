from app import db
from entities.user import User


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def save(user):
    db.session.add(user)
    db.session.commit()