from flask import Flask,render_template,redirect,request
from db.run_sql import run_sql
from models.author import Author


#CRUD

def save(author):
    sql = 'INSERT INTO authors (name) VALUES (%s) RETURNING *'
    values = [author.name]
    row = run_sql(sql,values)
    id = row[0]['id']
    author.id = id
    return author

def select_all():
    author_list = []
    sql = 'SELECT * FROM authors'
    rows = run_sql(sql)
    for row in rows:
        author = Author(row['name'],row['id'])
        author_list.append(author)
    return author_list

def select(id):
    author = None
    sql = 'SELECT * FROM authors WHERE id = %s'
    values = [id]
    result = run_sql(sql,values)[0]
    author = Author(result['name'],result['id'])
    return author 

def delete(id):
    sql = 'DELETE FROM authors WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM authors'
    run_sql(sql)