from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete book
- 'q' to quit

Your choice: """


def prompt_add_book():
    name = input("Please, enter the book name: ")
    author = input("Please, enter book's author name: ")
    database.add_book(name, author)


def prompt_list_books():
    books = database.get_all_books()
    for book in books:
        print(f"{book['name'].title()} is written by {book['author'].title()}. You {'already read' if  book['read'] else 'have not read'} this book.")


def prompt_mark_read():
    name = input("Please, enter the book name to mark read: ")
    database.read_book(name)


def prompt_delete_book():
    name = input("Please, enter the book name to delete: ")
    database.delete_book(name)


OPTIONS = {
    'a': prompt_add_book,
    'l': prompt_list_books,
    'r': prompt_mark_read,
    'd': prompt_delete_book
}


def menu():

    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        try:
            OPTIONS[user_input]()
        except KeyError:
            print("Unknown command please try again.")
        user_input = input(USER_CHOICE)


menu()
