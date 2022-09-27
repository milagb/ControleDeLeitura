from urllib.parse import _ResultMixinStr
from xml.dom.minidom import Identified
from flask import Blueprint, render_template
from flask import Flask, escape, request, redirect, url_for
from ..models.reading import Reading
from ..extensions import db
from ..models.books import Books


booksBp = Blueprint('livrosBp', __name__)

@booksBp.route('/books', methods=['GET', 'POST'])
def books_list():
    db.create_all()

    books_query = Books.query.all()
    

    # if request.method == 'POST':
    #     book_id=0
    #     book_query = Books.query.filter_by(id = book_id).first()
    #     print(book_query)

    #     db.session.add(book_query)   
    #     db.session.commit()

    return render_template('books.html', books = books_query, title='Books')


@booksBp.route('/reading', methods=['GET', 'POST'])
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

    # return render_template('insertbook.html', title='Insert New Books')
    return redirect(url_for('/books'))

@booksBp.route('/books/update/<book_id>', methods=['GET', 'POST'])
def update_book(book_id=0):
    # book_query = Books.query.filter_by(id = book_id).first()
    # print(book_query)
    
    if request.method == 'POST':
        book = Reading(book_id = book_id)
        db.session.add(book)   
        db.session.commit()

    return redirect(url_for("livrosBp.reading_list"))


@booksBp.route('/book/dlt/<book_id>', methods=['GET', 'POST'])
def dlt_book(book_id):
    if request.method == 'POST':
        book_query = Reading.query.filter_by(book_id = book_id).first()
        db.session.delete(book_query)   
        db.session.commit()

    return redirect(url_for("livrosBp.reading_list"))
  