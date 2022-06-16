from os import path
from tinydb import TinyDB

ROOT = path.dirname(path.relpath(__file__))

db = TinyDB(path.join(ROOT, "db.json"))

def create_post(id, name, content, creation_date):    
    db.insert({"id": id, "name": name, "content": content, "creation_date": creation_date})

def get_posts():
    return db.all()