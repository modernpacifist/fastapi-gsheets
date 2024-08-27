import sqlite3

from contextlib import contextmanager


db_filename = 'users.sqlite3'


# https://blog.hubspot.com/website/decorators-in-python#:~:text=Decorators%20with%20arguments%20provide%20additional,the%20modified%20function%20or%20class.
def authentication_decorator(func):
    def wrapper(*args, **kwargs):
        id = kwargs.get("id")
        if verify_user(id):
            return func(*args, **kwargs)
        else:
            raise PermissionError("User is not authenticated")
    return wrapper
# @authentication_decorator
# def restricted_function(user = None):
#     print("Access granted to the restricted function")
# restricted_function(user = "authenticated_user")


@contextmanager
def connect(db_name):
    conn = sqlite3.connect(db_name)
    try:
        cur = conn.cursor()
        yield cur

    except sqlite3.IntegrityError:
        print('User already in database')

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.commit()
        conn.close()


def verify_user(id):
    with connect(db_filename) as cur:
        if cur.execute(f'SELECT EXISTS(SELECT 1 FROM Users WHERE id = {id});').fetchone() == (0,):
            return False
        return True


def add_user(id, username):
    with connect(db_filename) as cur:
        cur.execute('INSERT INTO Users (id, username) VALUES (?, ?)', (id, username))


def get_all_users():
    with connect(db_filename) as cur:
        res = cur.execute('SELECT id FROM Users').fetchall()
    return res
