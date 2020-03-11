# The script prints two lists of odd and even numbers in a given range

received_value = None


# Function performs the ValueError check
def get_input_value(message):
    # Prompt user to enter a number of years
    received_value = input(message)

    # Check for ValueError
    while True:
        try:
            received_value = int(received_value)
            return int(received_value)
        except ValueError:
            print("You must enter a number!")
            received_value = input(message)


# Prompt user to enter the first number of the range
beginning_of_range = get_input_value("Please, enter a starting number of the range: ")
# Prompt user to enter the final numbers of the range
end_of_range = get_input_value("Please, enter a final number of the range: ")

# Create empty lists of odd and even numbers
odd_numbers = []
even_numbers = []

# Redistribute numbers into the odd and even lists
for i in range(int(beginning_of_range), int(end_of_range) + 1):
    if i % 2 == 1:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)

# Print the lists
print(f"Odd numbers are: {odd_numbers}")
print(f"Even numbers are: {even_numbers}")
