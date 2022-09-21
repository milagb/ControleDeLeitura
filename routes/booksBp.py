from urllib.parse import _ResultMixinStr
from flask import Blueprint, render_template
from flask import Flask, escape, request

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

    return render_template('reading.html', books = result, title='Reading')

@booksBp.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        form = request.form
        newBook = Books(name = form['InputBook_Name'], writer = form['InputWrite_Name'], 
        genre = form['InputGenre_Name'], release = form['InputRelease_Name'], 
        pages = form['InputPages_Name'], publisher = form['InputPublisher_Name'])
        
        db.session.add(newBook)   
        db.session.commit()

        # for key, value in request.form.items():
        #     print(f'{key}: {value}')

    return render_template('insertbook.html', title='Insert New Books')
    