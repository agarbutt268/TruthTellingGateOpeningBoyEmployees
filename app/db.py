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


#adds new user (username & password) into the database 
def add_new_user(username, password, phone_number, email, bio):
    
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db
    c = db.cursor() #creates db cursor to execute and fetch           

    c.execute("SELECT COUNT(user_id) FROM users")

    user_id = c.fetchone()

    data = (user_id, username, password, phone_number, email, bio)


    c.execute("INSERT INTO users VALUES(?,?,?,?,?,?)", data)
    db.commit()
    db.close()

    #checks whether the user already exists in the database
def check_user_exists(username):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor() #creates db cursor to execute and fetch      

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    dict = c.fetchone()

    db.close()

    if dict == None: #if no user
        return False
    
    return True #if dict is not empty (meaning user exists)

#gets the user's password from the database
def get_user_password(username):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db          
    c = db.cursor() #creates db cursor to execute and fetch      

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    dict = c.fetchone()

    db.close()

    return dict[2]

def get_user_id(username)
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db          
    c = db.cursor() #creates db cursor to execute and fetch      

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    dict = c.fetchone()

    db.close()

    return dict[0]