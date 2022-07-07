import secrets
import os
from books import app
from books import db
from books.models import Books
from flask import render_template, url_for, flash, redirect, request, abort
from books.forms import BookForm
from markupsafe import escape

@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    add_books = Books.query.all()
    for book in add_books:
        print(book.id)
    return render_template('home.html', add_books=add_books)

def save_picture(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/books_images", picture_fn)
    form_image.save(picture_path)
    return picture_fn


@app.route("/book/new", methods=['GET', 'POST'])
def new_book():
    form = BookForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.book_image.data)
        book = Books(title=form.title.data, author=form.author.data, series=form.series.data, no_of_books_in_series=form.no_of_books_in_series.data, book_in_series=form.book_in_series.data, book_image=picture_file )
        db.session.add(book)
        db.session.commit()
        flash('Your book has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_book.html', title='New Book',
                           form=form, legend='New Book')


@app.route("/book/<int:book_id>/delete", methods=['POST'])
def delete_book(book_id):
    book = Books.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))






