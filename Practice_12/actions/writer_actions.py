# Constructor for writer table functionality

# Import PrettyTable function
from Practice_12.helpers.output_helper import pretty_print
# Import the name of the table
from Practice_12.models.writer import TABLE_NAME
# Import functions needed for managing the table
from Practice_12.services.data_service import (get_data, execute_command)


# Function allows to view the table
def view_writers():
    # Create an SQL query to DB
    query = ("SELECT * FROM %s" % TABLE_NAME)
    # Assign the received data to variable
    writers = get_data(query)
    # Pretty print the list of writers
    pretty_print(writers)


# Function allows to add data to the table
def add_writer():
    while True:
        author = input('Please, enter Author name: ')

        if len(author.strip()) > 0:
            break

    query = ("INSERT INTO {} (name) VALUES ('{}')".format(TABLE_NAME, author))
    execute_command(query)
    print('Saved')
