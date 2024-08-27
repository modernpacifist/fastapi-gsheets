import sqlite3


CON = sqlite3.connect("users.db")
CURSOR = CON.cursor()

CURSOR.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER UNIQUE,
username TEXT NOT NULL
)
''')

CURSOR.commit()
CURSOR.close()
