from app import db
from datetime import date

lists_titles = db.Table(
    "Lists_Titles",
    db.Model.metadata,
    db.Column("list_id", db.Integer, db.ForeignKey("Lists.id"), primary_key=True),
    db.Column("title_id", db.Integer, db.ForeignKey("Titles.id"), primary_key=True),
)


class List(db.Model):
    __tablename__ = "Lists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    titles = db.relationship("Title", secondary=lists_titles)
    creation_date = db.Column(db.String(128), default=str(date.today()), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    user = db.relationship("User", back_populates="lists")
    public = db.Column(db.Boolean, default=False)

    def __init__(self, data):
        self.name = data.get("name")
        self.user = data.get("user")
        if "public" in data:
            self.public = bool(data.get("public"))

    def title_exists(self, title):
        return title.id in [t.id for t in self.titles]
