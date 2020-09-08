from app import db

watchlists_films = db.Table('Watchlists_Films', db.Model.metadata,
                       db.Column('watchlist_id', db.Integer, db.ForeignKey('Watchlists.id')),
                       db.Column('film_id', db.Integer, db.ForeignKey('Films.id'))
)

watchlists_shows = db.Table('Watchlists_Shows', db.Model.metadata,
                       db.Column('watchlist_id', db.Integer, db.ForeignKey('Watchlists.id')),
                       db.Column('show_id', db.Integer, db.ForeignKey('Shows.id'))
)


class Watchlist(db.Model):
    __tablename__ = "Watchlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    films = db.relationship("Film", secondary=watchlists_films)
    shows = db.relationship("Show", secondary=watchlists_shows)
    user = db.relationship("User", uselist=False, back_populates="watchlist")





