from app import db


class Episode(db.Model):
    __tablename__ = "Episodes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    show_id = db.Column(db.Integer, db.ForeignKey('Shows.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    release_date = db.Column(db.String(128), nullable=True)
    imdb_rating = db.Column(db.Float, nullable=True)
    user_rating = db.Column(db.Integer, nullable=True)

    def setter(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.release_date = data.get('release_date')
        self.imdb_rating = data.get('imdb_rating')
        self.user_rating = data.get('user_rating')
        self.show_id = data.get('show_id')

    def __init__(self, data):
        self.setter(data)
