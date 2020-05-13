from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from . import db



@app.route("/signup", methods=["POST"])
def create_user():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    #Chequeamos que no esté registrado
    user = db.execute("SELECT email FROM users WHERE email = :email",
                        {"email": email}).fetchone()
    if user: #Si hay usuario vamos a signup de nuevo  (En verdad debería ir al LOGIN
        flash('Email address already exists') #ver tutorial de login
        return redirect(url_for("auth.signup"))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.profile'))