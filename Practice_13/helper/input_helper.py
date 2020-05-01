# File consist of general purpose functions

# Colorama is used for producing colored terminal text and cursor positioning
from colorama import Fore
import datetime


# Function prompts user to enter string until it's done
def get_string(message):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        user_message = input(styled_message)
        user_message = user_message.strip()
        if len(user_message) > 1:
            return user_message


# Function prompts user to enter string description from 1 to 100 symbols until it's done
def get_description(message, max_length):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        user_message = input(styled_message)
        user_message = user_message.strip()
        if 1 < len(user_message) <= max_length:
            return user_message
        else:
            print(Fore.YELLOW + "Please, enter from 1 to 100 symbols!" + Fore.RESET)


# Function prompts user to enter number until it's done
def get_price(message, min_price):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        user_price = input(styled_message)

        try:
            price = float(user_price)
            assert price >= min_price
            return price
        except ValueError:
            print(Fore.YELLOW + "Please, enter a number" + Fore.RESET)
        except AssertionError:
            print(Fore.YELLOW + "Please, enter number greater than {}".format(min_price) + Fore.RESET)


# Function prompts user to enter number with minimal value until it's done
def get_age(message, min_val):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        user_age = input(styled_message)

        try:
            age = int(user_age)

            assert age >= min_val
            return age
        except ValueError:
            print(Fore.YELLOW + "Please, enter a number" + Fore.RESET)
        except AssertionError:
            print(Fore.YELLOW + "Please, enter number greater than {}".format(min_val) + Fore.RESET)


# Function prompts user to enter number with minimal and maximum value until it's done
def get_int(message, min_val, max_val):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    error_message = "{}Please, enter number greater than {} and smaller than {}!{}" \
        .format(Fore.YELLOW, min_val, max_val, Fore.RESET)
    while True:
        user_age = input(styled_message)

        try:
            number = int(user_age)

            assert max_val >= number >= min_val
            return number
        except ValueError:
            print(error_message)
        except AssertionError:
            print(error_message)


# Function prompts user to enter date until it's done
def get_date(message):
    styled_message = "{}{} (YYYY-MM-DD) {}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        str_date = input(styled_message)

        try:
            year, month, day = map(int, str_date.split('-'))
            new_date = datetime.date(year, month, day)
            return new_date
        except ValueError:
            print(Fore.YELLOW, "Please, enter correct date (YYYY-MM-DD): ", Fore.RESET)
