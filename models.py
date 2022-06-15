import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content, creation_date):
    connection = sql.connect(path.join(ROOT, "database.db"))
    cursor = connection.cursor()
    cursor.execute("insert into posts (name, content, creationdate) values(?, ?, ?)", (name, content, creation_date))
    connection.commit()
    connection.close()

def get_posts():
    connection = sql.connect(path.join(ROOT, "database.db"))
    cursor = connection.cursor()
    cursor.execute("select * from posts")
    posts = cursor.fetchall()
    return posts