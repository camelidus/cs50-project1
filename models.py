#! coding: utf-8
# import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func

import datetime

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    isbn = db.Column(db.String, nullable=False)
    pub_date = db.Column(db.Integer, nullable=False)
    # OJO ver airline4 de Lecture 4 (1:01 video 4) como hace método usando la relationship
   # reviews = db.relationship("Review", backref="book", lazy=True)

    # def add_review(self, name):
    #     p = Passenger(name=name, flight_id=self.id)
    #     db.session.add(p)
    #     db.session.commit()
    # def get_book_avg(self):
    #     book_avg = db.execute("SELECT AVG(rate) FROM review WHERE book_reviewed=self.id")
    #     return book_avg
    # def get_users_reviewed(self):
    #     users = db.execute("SELECT user_reviewed FROM review WHERE book_reviewed=self.id").fetchall()
    #     return users

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    #user_reviews = db.relationship("Review", backref="user", lazy=True)
    #user_reviews = db.Column(db.Integer, db.ForeignKey("reviews.id"))



class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    book_reviewed = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    user_reviewed = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    comment = db.Column(db.String(500), nullable=True)
    rate = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)



