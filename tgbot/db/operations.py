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


def add_user(id, username):
    try:
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Users (id, username) VALUES (?, ?)', (id, username))
        conn.commit()
        conn.close()

    except sqlite3.IntegrityError:
        print(f'User {id} - {username} already in database')
