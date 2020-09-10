from app import db


class Title(db.Model):
    __tablename__ = "Titles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    release_year = db.Column(db.Integer, nullable=True)
    stars = db.Column(db.String(256), nullable=True)
    genres = db.Column(db.String(128), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    country = db.Column(db.String(128), nullable=True)
    price = db.Column(db.Float, nullable=True)
    __mapper_args__ = {"polymorphic_on": type}


class Film(Title):
    __tablename__ = "Films"
    title_id = db.Column(db.Integer, db.ForeignKey("Titles.id"), primary_key=True)
    __mapper_args__ = {"polymorphic_identity": "Film"}
    director = db.Column(db.String(32), nullable=False)
    metascore = db.Column(db.Integer, nullable=True)
    duration = db.Column(db.Integer, nullable=True)


class Show(Title):
    __tablename__ = "Shows"
    title_id = db.Column(db.Integer, db.ForeignKey("Titles.id"), primary_key=True)
    __mapper_args__ = {"polymorphic_identity": "Show"}
    creator = db.Column(db.String(32), nullable=False)
    end_year = db.Column(db.Integer, nullable=True)
    episodes = db.relationship("Episode", foreign_keys="[Episode.show_id]")


class Episode(Title):
    __tablename__ = "Episodes"
    title_id = db.Column(db.Integer, db.ForeignKey("Titles.id"), primary_key=True)
    __mapper_args__ = {"polymorphic_identity": "Episode"}
    show_id = db.Column(db.Integer, db.ForeignKey("Shows.title_id"), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    season = db.Column(db.Integer, nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    show = db.relationship("Show", foreign_keys=[show_id])
