import sqlite3


# DB_PATH = "users.db"
connection = sqlite3.connect('users.sqlite3')


def add_user(id, username):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (id, username) VALUES (?, ?)', (id, username))
    connection.commit()
    connection.close()

