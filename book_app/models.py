

from . import db


class Author(db.Model):

    __tablename__ = "Roles"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    specialisation = db.Column(db.String(64))

    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation

    def __repr__(self):
        return f"<Author {self.name}>"


db.create_all()
