# Application for maintaining a library

# Import models of tables: book and writer
import Practice_12.models.book as book
import Practice_12.models.writer as writer
# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore
# This module adds explicit switch functionality to Python without changing the language
from switchlang import switch
# Import 2 classes we need to execute commands from user
from Practice_12.actions.book_actions import *
from Practice_12.actions.writer_actions import *
# Import sql setup to create a point of enter into DB
from Practice_12.services.data_service import (create_db)


# Main function manages commands from user and works with imports
def main():
    # Green header
    print(Fore.GREEN, "Books world", Fore.RESET)
    # Call the function to show available commands
    show_commands()

    # Prompt user to choose action util exit
    while True:
        # Call the function and assign the command from user to the variable
        action = get_action()
        # Pass the variable to the function to execute functions from imports
        with switch(action) as s:
            # All commands from user get appropriate functionality
            # Call imported functions from class instances
            s.case('b', books_list)
            s.case('i', get_book_info)
            s.case('r', add_book)

            s.case('l', view_writers)
            s.case('w', add_writer)
            s.case('?', show_commands)

            s.case('e', exit)
            s.default(lambda: print('Sorry, this is unknown command'))


# Function creates a list of available commands
def show_commands():
    print(Fore.LIGHTYELLOW_EX, "What would you like to do:", Fore.RESET)

    # Managing books
    print(Fore.LIGHTMAGENTA_EX, "[B]ooks list", Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX, "Book [i]nfo", Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX, "[R]egister book", Fore.RESET)

    # Managing writers
    print(Fore.LIGHTCYAN_EX, "Writer [l]ist", Fore.RESET)
    print(Fore.LIGHTCYAN_EX, "Register a [w]riter", Fore.RESET)

    # Managing miscellaneous
    print(Fore.LIGHTRED_EX, "[?] Help (this info)", Fore.RESET)
    print(Fore.LIGHTRED_EX, "[e] Exit", Fore.RESET)


# Function prompts user to enter a command and returns the letter
def get_action():
    action = input(Fore.YELLOW + '> ' + Fore.RESET)
    return action.strip().lower()


# Launcher of the script
if __name__ == '__main__':
    # Create DataBase with 2 tables: writer and book
    create_db(writer.TABLE, book.TABLE)
    main()
