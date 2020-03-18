# The script prints a letter from the alphabet and the letters, located before and after it

# Create a list of letters in alphabet
import string

alphabet = list(string.ascii_lowercase)

input_letter = None

# While input is not a latin letter, keep prompting
while input_letter not in alphabet:
    input_letter = input("Please, enter a letter: ").lower()

# Let's find out the index of the letter and get the indexes of the previous and next letters
if input_letter in alphabet:
    previous_letter = alphabet[alphabet.index(input_letter) - 1]
    try:
        next_letter = alphabet[alphabet.index(input_letter) + 1]
    except IndexError:
        next_letter = alphabet[0]

    # Let's print all 3 letters
    print(f"Your letter is {input_letter}")
    print(f"Previous letter is {previous_letter}")
    print(f"Next letter is {next_letter}")
