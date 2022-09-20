from unicodedata import name
from ..extensions import db

class Books(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    writer = db.Column(db.String(200))
    genre = db.Column(db.String(200))
    release = db.Column(db.String(50))
    pages = db.Column(db.String(50))
    publisher = db.Column(db.String(200))


    def __repr__(self):
        return "<Books(name={}, writer={}, genre={}, release={}, pages={}, publisher={})>".format(self.name, self.writer, self.genre, self.release, self.pages, self.publisher)

    