# Constructor for guest functionality

# Import PrettyTable function
from Practice_13.helper.output_helper import pretty_print
# Import class Guest for creating instances
from Practice_13.models.guests import Guest
# Import general purpose functions
from Practice_13.helper.input_helper import get_string, get_age
# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore


class GuestService:

    def guest_list(self):
        print(Fore.MAGENTA, "Guests list", Fore.RESET)

        # Create instance of Apartment class
        guests = Guest.objects()
        # Create 3 columns of table
        columns = ('Name', 'Age', 'Is_card')
        # Print table
        pretty_print(guests, columns)

    # Function creates new guest with 2 parameters: name and age, which is limited to 18
    def add_guest(self):
        print(Fore.MAGENTA, "Add guest", Fore.RESET)
        # Prompt user to enter name and age of new guest
        name = get_string("Please, enter the name of the guest: ")
        age = get_age("Please, enter the age of the guest: ", min_val=Guest.age.min_value)

        # Create an instance of guest class
        guest = Guest(name=name, age=age)
        # Save newly created guest
        guest.save()

        print(Fore.GREEN, "Guest added", Fore.RESET)
