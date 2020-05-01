# Constructor for apartment functionality

# Import class Apartment for creating instances
from Practice_13.models.apartments import Apartment
# Import general purpose functions
from Practice_13.helper.input_helper import get_string, get_description, get_price
# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore
# Import PrettyTable function
from Practice_13.helper.output_helper import pretty_print


class ApartmentService:

    # Function prints table with list of apartments
    def apartments_list(self):
        print(Fore.MAGENTA, "Apartments list", Fore.RESET)

        # Create instance of Apartment class
        apartments = Apartment.objects()
        # Create 3 columns of table
        columns = ('Name', 'Description', 'Price')
        # Print table
        pretty_print(apartments, columns)

    # Function adds a new apartment
    def add_apartment(self):
        print(Fore.MAGENTA, "Add apartment", Fore.RESET)

        # Create instance of Apartment object
        apartment = Apartment()
        # Prompt user to fill necessary fields
        apartment.name = get_string("Please, enter a name of apartment: ")
        apartment.description = get_description(
            "Please, enter a description of apartment: ",
            max_length=Apartment.description.max_length
        )
        apartment.price = get_price("Please, enter a price of apartment: ", min_price=Apartment.price.min_value)

        # Save newly created apartment
        apartment.save()

        print(Fore.GREEN, "Apartment saved", Fore.RESET)

    # Function searches apartment by name
    def search_apartment(self):
        print(Fore.MAGENTA, "Apartment search result", Fore.RESET)

        name = get_string("Please, enter the name of apartment: ")

        apartment = Apartment.objects().filter(name=name)

        # Create 3 columns of table
        columns = ('Name', 'Description', 'Price')
        # Print table
        pretty_print(apartment, columns)
        return apartment
