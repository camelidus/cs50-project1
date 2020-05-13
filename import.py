#! coding: utf-8
#Acá importamos el csv books.csv "python3 import.py"
import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request
from models import *

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

def main():
    b = open("books.csv")
    reader = csv.reader(b)
    next(reader, None)
    for isbn, title, author, year in reader:
       #Ver sintaxis en SQL en archivo import0.py Lect 4
        db.execute("INSERT INTO books (isbn, title, author, pub_date) VALUES (:isbn, :title, :author, :pub_date )",
                   {"isbn": isbn, "title": title, "author": author, "pub_date":year})
        print(f"Added book {title} written by {author} in {year}. ISBN > {isbn}")
    db.commit()

        #book = Book(isbn=isbn, title=title, author=author, year=year)
        #db.session.add(book)

   # db.session.commit()

if __name__ == "__main__":
    main()

# al ser sql comandos no hay app de flask
# if __name__ == "__main__":
#     with app.app_context():
#         main()
