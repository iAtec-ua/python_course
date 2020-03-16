# The script creates a list of 20 numbers and processes it

import random

# Create a random list of 20 numbers, all even numbers are negative
random_list = []

for i in range(1, 21):
    if i % 2 == 1:
        number = random.randrange(0, 100)
        random_list.append(number)
    else:
        number = random.randrange(0, 100)
        random_list.append(-number)

print(random_list)

# Prompt a number
user_number = input("Please, enter a number in range 0 - 99: ")

# Count the number of time the number appears in the list
appear = random_list.count(int(user_number))
print(f"Your number {user_number} appears {appear} times in the list!")
