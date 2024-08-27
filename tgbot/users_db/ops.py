import sqlite3


# DB_PATH = "users.db"


def verify_user(id):
    conn = sqlite3.connect('users.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM Users WHERE (id) = (?);', (id))
    conn.commit()
    conn.close()


def add_user(id, username):
    conn = sqlite3.connect('users.sqlite3')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Users (id, username) VALUES (?, ?)', (id, username))
    conn.commit()
    conn.close()
