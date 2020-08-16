from app import db


class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    lists = db.relationship("List", back_populates="user")
    watchlist_id = db.Column(db.Integer, db.ForeignKey('Watchlists.id'))
    watchlist = db.relationship("Watchlist", back_populates="user")

    def __init__(self, data):
        self.username = data.get('username')
        self.fullname = data.get('fullname')
        self.password = data.get('password')