#! coding: utf-8
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

#Con esta línea ,e aseguro que este método se corra solo cuando ejecuto este archivo y que no se corra si llegara a importar
#este archivo desde otro lado,
#Ojo estas lineas permiten que ejecute desde la consola, sino no te deja!
if __name__ == "__main__":
    with app.app_context():
        main()