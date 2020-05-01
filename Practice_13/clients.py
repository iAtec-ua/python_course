# Application for maintaining a hotel, managing apartments, guests and reservations

# Import mongo setup to create a point of enter into MongoDB
import Practice_13.services.mongo_setup as db_setup
# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore
# This module adds explicit switch functionality to Python without changing the language
from switchlang import switch
# Import 3 classes we need to execute commands from user
from Practice_13.services.apartment_service import ApartmentService
from Practice_13.services.guest_service import GuestService
from Practice_13.services.reservation_service import ReservationService


# Main function manages commands from user and works with imports
def main():
    # Create connection to MongoDB
    db_setup.global_init()
    # Blue header
    print(Fore.BLUE, "Hotel service", Fore.RESET)
    # Call the function to show available commands
    commands()

    # Create instances of 3 classes
    apartments = ApartmentService()
    guests = GuestService()
    reservations = ReservationService()

    # Prompt user to choose action util exit
    while True:
        # Call the function and assign the command from user to the variable
        action = get_action()
        # Pass the variable to the function to execute functions from imports
        with switch(action) as s:
            # All commands from user get appropriate functionality
            # Call imported functions from class instances
            s.case('l', apartments.apartments_list)
            s.case('a', apartments.add_apartment)
            s.case('s', apartments.search_apartment)

            s.case('v', guests.guest_list)
            s.case('g', guests.add_guest)

            s.case('b', reservations.view_reservations)
            s.case('m', reservations.add_reservations)

            s.case('?', commands)
            s.case('e', exit)

            s.default(lambda: print("This is unknown command"))


# Function creates a list of available commands
def commands():
    print(Fore.LIGHTYELLOW_EX, "What action would you like to perform?", Fore.RESET)

    # Managing apartments
    print(Fore.LIGHTMAGENTA_EX, "Apartments [l]ist", Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX, "[A]dd apartment", Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX, "[S]earch apartment", Fore.RESET)

    # Managing guests
    print(Fore.LIGHTCYAN_EX, "[V]iew guests", Fore.RESET)
    print(Fore.LIGHTCYAN_EX, "Add [g]uest", Fore.RESET)

    # Managing reservations
    print(Fore.LIGHTBLUE_EX, "[B]ooking info", Fore.RESET)
    print(Fore.LIGHTBLUE_EX, "[M]ake reservation", Fore.RESET)

    # Managing miscellaneous
    print(Fore.LIGHTRED_EX, "[?] Help (this info)", Fore.RESET)
    print(Fore.LIGHTGREEN_EX, "[E]xit", Fore.RESET)


# Function prompts user to enter a command and returns the letter
def get_action():
    print(Fore.YELLOW + ">" + Fore.RESET)
    action = input()
    return action.strip().lower()


# Point of entering the application, executing line, marks the main module
if __name__ == '__main__':
    main()
