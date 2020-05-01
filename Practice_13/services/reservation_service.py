# Constructor for reservations functionality

# import datatime for time management
import datetime
# Import class Reservation for creating instances
from Practice_13.models.reservations import Reservation
# Import general purpose functions
from Practice_13.helper.input_helper import get_int, get_date
# Import ApartmentService class to get access to apartment searching function
from .apartment_service import ApartmentService
# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore
# Import PrettyTable function
from Practice_13.helper.output_helper import pretty_print
# Import class Apartment for creating instances
from Practice_13.models.apartments import Apartment


# from typing import List, Optional

class ReservationService:

    def view_reservations(self):
        print(Fore.MAGENTA, "View reservations", Fore.RESET)

        apartments = Apartment.objects()
        reservations = Apartment.reservations
        for room in apartments:
            apartments.append(reservations)

        # Print results and duration of booking
        columns = ('Name', 'Description', 'Price', 'Check_in_date', 'Check_out_date', 'Booked_date')
        # Print table
        pretty_print(apartments, columns)

    def add_reservations(self):
        print(Fore.MAGENTA, "Add reservations", Fore.RESET)

        ApartmentService.apartments_list(self)

        # Search apartment by name
        # apartment_search = ApartmentService()
        apartments = ApartmentService().search_apartment()

        # Check if the list of apartments is empty
        if not apartments or len(apartments) == 0:
            print(Fore.YELLOW, "Apartments not found", Fore.RESET)
            return

        # Get the index of the apartment
        # row_idx = get_int("Please, enter apartment number: ", 0, len(apartments))

        # Create apartment using entered index
        apartment = apartments[0]

        # Create instance of Reservation class
        reservation = Reservation()

        # Create date of reservation
        reservation.booked_date = datetime.datetime.now()

        # Create dates of check-in and check-out
        reservation.check_in_date = get_date("Please, enter check-in date: ")
        reservation.check_out_date = get_date("Please, enter check-out date: ")

        # Make changes in apartment which was booked
        apartment.reservations.append(reservation)
        # Save changes
        apartment.save()

        # Print results and duration of booking
        columns = ('Check_in_date', 'Check_out_date', 'Booked_date')
        # Print table
        pretty_print([reservation], columns)
        print("{}Booking duration is {} day(s).{}".format(Fore.MAGENTA, reservation.duration, Fore.RESET))

        print(Fore.GREEN, "Reservation saved!", Fore.RESET)
