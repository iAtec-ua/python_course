# The script calculates deposit interest taking first deposit, number of years and rate from user

received_value = None


# Function performs the ValueError check
def get_input_value(message):
    # Prompt user to enter a number of years
    received_value = input(message)

    # Check for ValueError
    while True:
        try:
            received_value = float(received_value)
            return float(received_value)
        except ValueError:
            print("You must enter a number!")
            received_value = input(message)


# Prompt the necessary data
first_deposit = get_input_value("Please, enter a first deposit: ")
rate = get_input_value("Please, enter a rate: ")
years_number = get_input_value("Please, enter a number of years: ")

# Declare initial variables
interest = 0
deposit = float(first_deposit)
rate = float(rate)
print(f"You want to deposit ${first_deposit} for {years_number} years with {rate}% rate")

# Calculate interests and step deposits
for year in range(1, int(years_number) + 1):
    interest = float(deposit * rate / 100)
    deposit += interest
    print(f"After {year} years, your interest will be ${interest} and your deposit will grow up to ${deposit}")
