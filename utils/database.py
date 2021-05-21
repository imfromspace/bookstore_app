"""
Concerned with storing and retrieving books from a SQLite database.
"""
from .database_connection import DatabaseConnection


def _execute_db_query(query, *args):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        res = cursor.fetchall()
    return res


def create_book_table():
    _execute_db_query('CREATE TABLE IF NOT EXISTS books(NAME TEXT PRIMARY KEY, AUTHOR TEXT, READ INTEGER)')


def add_book(name, author):
    try:
        _execute_db_query('INSERT INTO books VALUES(?, ?, 0)', name, author)
    except Exception:
        print("This book is already in database.")


def read_book(name):
    _execute_db_query("UPDATE books SET READ='1' WHERE NAME=?", name)


def delete_book(name):
    _execute_db_query("DELETE FROM books WHERE NAME=?", name)


def get_all_books():
    books = [{'name': row[0], 'author': row[1], 'read': True if row[2] == 1 else False} for row in _execute_db_query("SELECT * FROM books")]
    return books


class BookNotFound(Exception):
    pass
