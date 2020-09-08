from app import db

lists_films = db.Table('Lists_Films', db.Model.metadata,
                       db.Column('list_id', db.Integer, db.ForeignKey('Lists.id')),
                       db.Column('film_id', db.Integer, db.ForeignKey('Films.id'))
)

lists_shows = db.Table('Lists_Shows', db.Model.metadata,
                       db.Column('list_id', db.Integer, db.ForeignKey('Lists.id')),
                       db.Column('show_id', db.Integer, db.ForeignKey('Shows.id'))
)


class List(db.Model):
    __tablename__ = "Lists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    films = db.relationship("Film", secondary=lists_films)
    shows = db.relationship("Show", secondary=lists_shows)
    creation_date = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    user = db.relationship("User", back_populates="lists")

    def __init__(self, data):
        self.name = data.get('name')
        self.creation_date = data.get('creation_date')
        self.user = data.get('user')


