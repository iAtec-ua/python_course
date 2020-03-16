# The script shows the number of days in a given month and tells if the day is a weekday or weekend

# Import calendar module
import calendar

# Prompt a user to enter a date
date = input("Please, enter a date (DD-MM-YYYY): ")

# Decide if the day is a weekday or weekend
date_list = date.split("-")
day_number = calendar.weekday(int(date_list[2]), int(date_list[1]), int(date_list[0]))
if day_number < 5:
    print(f"This day ({date}) is a weekday!")
else:
    print(f"This day ({date}) is a weekend!")

# Find out the number of days in the month
number_of_days = calendar.monthrange(int(date_list[2]), int(date_list[1]))
print(f"The number of days in the month is {number_of_days[1]}!")