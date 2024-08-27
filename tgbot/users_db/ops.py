import sqlite3


# DB_PATH = "users.db"
connection = sqlite3.connect('users.db')


def add_user(id, username):
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO Users (id, username) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()
    return None
