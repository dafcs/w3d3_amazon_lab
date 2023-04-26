import author_repository as author_repo
from models.author import Author
from models.book import Book
from flask import Flask,render_template,redirect,request
from db.run_sql import run_sql


def save(book):
    sql = 'INSERT INTO books (title,author_id) VALUES (%s,%s) RETURNING *'
    values = [book.title,book.author.id]
    row = run_sql(sql,values)
    id = row[0]['id']
    book.id = id
    return book

def select_all():
    book_list = []
    sql = 'SELECT * FROM books'
    rows = run_sql(sql)
    for row in rows:
        book = book(row['title'],row['author_id'],row['id'])
        book_list.append(book)
    return book_list

def select(id):
    book = None
    sql = 'SELECT * FROM books WHERE id = %s'
    values = [id]
    result = run_sql(sql,values)[0]
    book = book(result['title'],result['author_id'],result['id'])
    return book 

def delete(id):
    sql = 'DELETE FROM books WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM books'
    run_sql(sql)