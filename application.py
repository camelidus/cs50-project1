#! coding: utf-8
import os

from flask import Flask, session, Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#OJO No olvidarse pasar las variables al template!

# @app.route("/")
# def index():
# #    user = session.user_id
#     #if not user:
#
#     return "Project 1: TODO. mira vos"
@app.route("/")
def index():
    # books = Book.query.all()
    books = db.execute("SELECT * FROM books ORDER BY pub_date ASC").fetchall()

    return render_template("index.html", books=books)

@app.route("/login")
def login():
    return render_template("login.html")
