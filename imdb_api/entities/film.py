from app import db


class Film(db.Model):
    __tablename__ = "Films"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    release_date = db.Column(db.String(128), nullable=True)
    stars = db.Column(db.String(256), nullable=True)
    genres = db.Column(db.String(128), nullable=True)
    director = db.Column(db.String(128), nullable=True)
    imdb_rating = db.Column(db.Float, nullable=True)
    metascore = db.Column(db.Integer, nullable=True)
    country = db.Column(db.String(128), nullable=True)

    def setter(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.release_date = data.get('release_date')

        stars_list = data.get('stars')
        self.stars = ""
        for star in stars_list:
            self.stars += star + ", "

        genres_list = data.get('genres')
        self.genres = ""
        for genre in genres_list:
            self.genres += genre + ", "

        self.director = data.get('director')
        self.imdb_rating = data.get('imdb_rating')
        self.user_rating = data.get('user_rating')
        self.metascore = data.get('metascore')

    def __init__(self, data):
        self.setter(data)