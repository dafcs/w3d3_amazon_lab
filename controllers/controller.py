from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo

tasks_blueprint = Blueprint("books", __name__)

@tasks_blueprint.route('/books')
def books_():
    books = book_repo.select_all()
    return render_template('books/books.jinja',books = books)

@tasks_blueprint.route('/books/<id>/delete', methods = ['POST'])
def books_delete(id):
    book_repo.delete(id)
    return redirect('/books')

@tasks_blueprint.route('/books/new')
def add_book_form():
    authors = author_repo.select_all()
    return render_template('/books/new.jinja',authors = authors)

# @tasks_blueprint.route('/books/new', methods = ['POST'])
# def add_book_form(book):
#     book_title = request.form['title']
#     book_author = author_repo.select(request.form['author'])
#     book = Book(book_title,book_author)
#     book_repo.save(book)
#     return redirect('/books')