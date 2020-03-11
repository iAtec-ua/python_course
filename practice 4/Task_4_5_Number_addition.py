# The script takes a number from user, prints it, summarises and counts its digits

# Prompt user to enter a number
input_number = input("Please, enter a number: ")

# Check for ValueError
while True:
    try:
        int(input_number)
        # Create a list of digits
        number_list = list(input_number)
        # Count the number of digits
        count = len(input_number)
        # Summarize the digits of the number
        total = 0
        # Calculate the output
        for i in range(count):
            total = total + int(input_number[i])
        # Print the needed data
        print(f"""Your number is: {input_number}
        Total of its digits is: {total} 
        It has {count} digits""")
        break
    except ValueError:
        # Not a valid number
        print("You must enter an integer!")
        input_number = input("Please, enter a number: ")
