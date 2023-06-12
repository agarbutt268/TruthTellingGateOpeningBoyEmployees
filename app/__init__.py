from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import requests
import os
import db

app = Flask(__name__)
app.secret_key = "aiushdvaioudshvaoiudhcaiodhc"

db.reset_database()
db.add_new_user("Aden Garbutt", "1738", "phone_number", "email", "bio")
db.add_new_user("Emerson Gelobter", "123", "phone_number", "email", "bio")
db.add_new_user("Adele Bois", "123", "phone_number", "email", "bio")
db.add_new_user("Adam Sherer", "123", "phone_number", "email", "bio")
db.add_new_user("Martin Iglesias", "123", "phone_number", "email", "bio")


@app.route('/', methods=['GET', 'POST'])
def home():

    if not 'username' in session:
        return render_template('login.html')

    f = db.select_all_users()

    return render_template('home.html', friends = f, username = session['username'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))

    user = request.form['username_login']
    pw = request.form['password_login']

    if db.check_user_exists(user):

        if str(db.get_user_password(user)) == str(pw):
            session['username'] = user
            return redirect(url_for('home'))

    return render_template('login.html', error="user or password incorrect")


@app.route('/register', methods=['POST'])
def register():
    user = request.form['username_register']
    pw = request.form['password_register']
    pw2 = request.form['password2_register']

    if db.check_user_exists(user):
        return render_template('login.html', error="user already exists")

    else:
        if pw == pw2:
            db.add_new_user(user, pw, "915-345-1324", "hello@gmail.com", "hi my names is aden")
            session['username'] = user
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="passwords must match")



@app.route('/mutuals')
def mutuals():

    return render_template('mutuals.html', friends = ["jd", "adele", "emerson", "aden"])


@app.route('/friends')
def friends():

    return render_template('mutuals.html', friends = ["jd", "adele", "emerson", "aden"])


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.run()
