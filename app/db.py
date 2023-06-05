import sqlite3
import csv

DB_FILE = "geronimo.db"

def refet_database():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db
    c = db.cursor() #creates db cursor to execute and fetch           

    c.execute("DROP TABLE IF EXISTS users;")
    c.execute("DROP TABLE IF EXISTS friends;")
    c.execute("DROP TABLE IF EXISTS messages;")

    c.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username STRING, password STRING, phone_number STRING, e-mail STRING, bio STRING);")
    c.execute("CREATE TABLE IF NOT EXISTS friends(pair_id INTEGER, friend_0_id INTEGER, friend_1_id INTEGER);")
    c.execute("CREATE TABLE IF NOT EXISTS messages(date STRING, time STRING, sequence_id INTEGER, pair_id INTEGER, message STRING);")

    db.commit()
    db.close()