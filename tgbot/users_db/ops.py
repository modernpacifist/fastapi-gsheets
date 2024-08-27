import sqlite3


def verify_user(id):
    try:
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()
        a = cursor.execute(f'SELECT EXISTS(SELECT 1 FROM Users WHERE id = {id});').fetchone()
        conn.commit()
        conn.close()

        if not a:
            return False
        return True

    except Exception as e:
        print(e)
        return False


def add_user(id, username):
    try:
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Users (id, username) VALUES (?, ?)', (id, username))
        conn.commit()
        conn.close()

    except sqlite3.IntegrityError:
        print(f'User {id} - {username} already in database')
