# Constructor for book table functionality

# Import PrettyTable function
from Practice_12.helpers.output_helper import pretty_print
# Import the names of the tables
from Practice_12.models.book import TABLE_NAME as BOOK_TABLE_NAME
from Practice_12.models.writer import TABLE_NAME as WRITER_TABLE_NAME
# Import functions needed for managing the table
from Practice_12.services.data_service import (get_data, execute_command)
# Import function to have an opportunity to choose from the list of writers
from Practice_12.actions.writer_actions import view_writers


# Function shows the full list of the books and their authors
def books_list():
    # Create an SQL query to DB
    query = ("SELECT * FROM {}".format(BOOK_TABLE_NAME))
    # Assign the received data to variable
    book_info = get_data(query)
    # Create an SQL query to DB
    query1 = ("SELECT * FROM {}".format(WRITER_TABLE_NAME))
    # Assign the received data to variable
    writer_info = get_data(query1)
    # Create a variable for iterating the dictionary
    counter = len(book_info)
    # iterate the dictionary to match authors with the books
    for i in range(counter):
        id_writer = book_info[i]['writerId']
        book_info[i]["writerId"] = writer_info[id_writer - 1]["name"]
        i += 1
    # Change the header of the column
    book_info[0]["Author"] = book_info[0].pop("writerId")
    # Pretty print the list of writers
    pretty_print(book_info)


# Function shows info about a book which name is given by user
def get_book_info():
    # Prompt user to enter the name of the book
    while True:
        user_book = input("Please, enter the name of the book: ")

        if len(user_book.strip()) > 0:
            break

    # Create an SQL query to DB
    query = ("SELECT * FROM {} WHERE name='{}'".format(BOOK_TABLE_NAME, user_book))
    # Assign the received data to variable
    book_info = get_data(query)
    # Change the header of the column
    book_info[0]["Author"] = book_info[0].pop("writerId")
    # Assign id of the author to the variable
    id_writer = book_info[0]["Author"]
    # Create an SQL query to DB
    query1 = ("SELECT name FROM {} WHERE id='{}'".format(WRITER_TABLE_NAME, id_writer))
    # Assign the received data to variable
    writer_info = get_data(query1)
    # Change the content of the chunk
    book_info[0]["Author"] = writer_info[0]["name"]

    if not book_info:
        print("There is no book with this name")
    else:
        # Pretty print the list of writers
        pretty_print(book_info)


# Function allows adding new books
def add_book():
    # Prompt user to enter the name of the book
    while True:
        book_name = input("Please, enter the name of the book: ")

        if len(book_name.strip()) > 0:
            break

    # Prompt user to enter the description of the book
    book_description = input("Please, enter the description of the book: ")

    view_writers()

    # Prompt user to enter the author's id provided a list of the writers
    while True:
        writer_id = int(input("Please, enter writer's id: "))
        break

    # Create an SQL query to DB
    query = ("INSERT INTO {} (name, description, writerId) VALUES ('{}', '{}','{}')"
             .format(BOOK_TABLE_NAME, book_name, book_description, writer_id)
             )
    execute_command(query)

    print('Saved')
