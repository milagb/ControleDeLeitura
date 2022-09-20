from ..extensions import db

class Read(db.Model):
    __tablename__ = "booklist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    livro = db.Column(db.String(200))
    autor = db.Column(db.String(200))
    genero = db.Column(db.String(200))
    lancamento = db.Column(db.String(50))
    paginas = db.Column(db.String(50))
    editora = db.Column(db.String(200))


    def __repr__(self):
        return "<Read(livro={}, autor={}, genero={}, lancamento={}, paginas={}, editora={})>".format(self.livro, self.autor, self.genero, self.lancamento, self.paginas, self.editora)