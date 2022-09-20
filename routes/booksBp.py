from flask import Blueprint, render_template

from ..models.reading import Reading
from ..extensions import db
from ..models.books import Books


booksBp = Blueprint('livrosBp', __name__)

@booksBp.route('/books')
def books_list():
    db.create_all()
    books_query = Books.query.all()
    print(books_query)
    return render_template('books.html', books = books_query)

@booksBp.route('/reading')
def reading_list():
    db.create_all()
    # books_query = Reading.query.all()
    # books_query = Reading.join(Books).all()
    books_query = db.session.query(Books, Reading).join(Reading, Reading.book_id == Books.id).all()
    print(books_query)
    books_query[0] = books_query[0][0]
    return render_template('books.html', books = books_query)
    