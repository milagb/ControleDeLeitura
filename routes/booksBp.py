from urllib.parse import _ResultMixinStr
from flask import Blueprint, render_template

from ..models.reading import Reading
from ..extensions import db
from ..models.books import Books


booksBp = Blueprint('livrosBp', __name__)

@booksBp.route('/books')
def books_list():
    db.create_all()

    books_query = Books.query.all()
    return render_template('books.html', books = books_query, title='Books')

@booksBp.route('/reading')
def reading_list():
    db.create_all()

    books_query = db.session.query(Books, Reading).join(Reading, Reading.book_id == Books.id).all()
    
    result = []
    for tuple in books_query:   
        result.append(tuple[0])

    return render_template('books.html', books = result, title='Reading')

@booksBp.route('/insertbook')
def insertbook_list():

    return render_template('insertbook.html')
    
    