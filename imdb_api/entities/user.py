from app import db
import flask_bcrypt


class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    lists = db.relationship("List", back_populates="user")
    titles = db.relationship("UserTitle")

    def __init__(self, data):
        self.username = data.get("username")
        self.fullname = data.get("fullname")
        self.password = User.hash_password(data.get("password"))
        self.role = data.get("role")

    @staticmethod
    def hash_password(pswd):
        pwd_hash = flask_bcrypt.generate_password_hash(pswd)
        return pwd_hash.decode("utf8")

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)


class UserTitle(db.Model):
    __tablename__ = "Users_Titles"

    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), primary_key=True)
    title_id = db.Column(db.Integer, db.ForeignKey("Titles.id"), primary_key=True)
    title = db.relationship("Title")
    rate = db.Column(db.Integer, nullable=True)
    on_watchlist = db.Column(db.Boolean, default=False)
    purchased = db.Column(db.Boolean, default=False)
