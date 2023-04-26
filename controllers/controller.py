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