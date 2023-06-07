from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import requests

app = Flask(__name__)

@app.route('/')
def home():
    if not 'user_id' in session:
        return redirect(url_for('login'))

    return render_template('home.html')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/mutuals')
def mutuals():

    return render_template('mutuals.html', friends = ["jd", "adele", "emerson", "aden"])

if __name__ == '__main__':
    app.debug = True
    app.run()
