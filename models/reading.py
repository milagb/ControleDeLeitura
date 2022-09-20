from ..extensions import db

class Reading(db.Model):
    __tablename__ = "reading"
    book_id = db.Column(db.Integer, primary_key=True, foreign_key="books.id")
    
    def __repr__(self): 
        #TODO 
        return ""

    