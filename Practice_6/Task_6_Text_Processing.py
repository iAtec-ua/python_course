# Script processes a given text in different ways

# Create a list of letters in alphabet
import string

alphabet = list(string.ascii_lowercase)

# This is the text
given_text = """Etiam in porta mauris, ut lacinia dui. Suspendisse maximus ipsum purus, vitae cursus mauris blandit eu. Integer tempor non neque eget eleifend. Morbi id nulla nec lectus lobortis imperdiet eget mollis enim. Donec sed quam a mi maximus suscipit lacinia vel sapien. Vivamus dolor nisl, interdum eget porttitor in, malesuada ut mi. Nam ac fermentum velit, non gravida sem. Nullam ante leo, volutpat vel sapien nec, dignissim faucibus lacus. Proin sed ligula vitae est porttitor vulputate convallis sed mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent viverra, ante eget ultricies venenatis, nulla mauris euismod velit, vitae pretium neque massa at nunc. Nulla id dictum nunc. Integer efficitur dictum felis sed maximus. Cras ultrices erat vitae mauris rhoncus blandit. Morbi ultrices at elit vel dignissim. Etiam libero risus, mattis iaculis magna ac, egestas varius odio. Nam viverra quam id purus pulvinar, ac interdum diam tincidunt. In pulvinar nibh sit amet purus dignissim, et porttitor libero dapibus. Nunc non nisi vel mi iaculis placerat. Proin porttitor sapien dui, at tempor dolor egestas ac. Phasellus eleifend tellus eu mauris dictum sollicitudin ac ut quam. Aliquam auctor erat vitae diam bibendum feugiat. Mauris ut dolor id ante feugiat lobortis. Duis in quam cursus, tincidunt lorem at, sagittis libero. Mauris tortor nisi, efficitur sit amet sapien sit amet, ultrices lacinia mi. Nulla facilisi. Nullam laoreet tortor id ante interdum, non tempus ante gravida. Integer nec volutpat odio, vitae ullamcorper est. Etiam ligula dui, convallis et blandit vitae, varius vitae mauris. Mauris vitae pellentesque justo, a ullamcorper metus. Maecenas porttitor massa vitae tortor interdum, aliquam rutrum tellus tincidunt. Sed vehicula felis a leo tempus, in fermentum turpis elementum. Pellentesque non sodales nulla, eget efficitur neque. In hac habitasse platea dictumst. Vivamus nec ultrices est. Fusce ac erat sed lectus egestas consequat. Sed scelerisque nisi sem, ut dictum diam efficitur laoreet. Integer aliquam in mauris in varius. Sed eget tempus ex. Praesent nec neque eu erat dapibus lacinia id quis nulla.
Praesent quam diam, volutpat at velit sed, ultricies tincidunt nunc. Etiam metus lorem, rutrum et sollicitudin eget, dictum feugiat augue. Sed quis libero at turpis lobortis gravida. Nunc congue eget ipsum eget euismod. Cras odio nulla, sollicitudin imperdiet diam vel, pellentesque congue nunc. Nunc a odio eu mauris blandit placerat at sit amet turpis. Donec eget mattis felis. Sed dui odio, tincidunt eget ullamcorper non, ornare eget libero. Morbi eu lorem bibendum, pharetra sem id, condimentum mauris. Integer volutpat pharetra mauris ut hendrerit. Interdum et malesuada fames ac ante ipsum primis in faucibus."""

# Transfer the text into low case
lowcase_text = given_text.lower()

# Create a list of unwanted characters
bad_char = [",", ".", "!", "?"]

# Delete the unwanted characters from the text
for i in bad_char:
    lowcase_text = lowcase_text.replace(i, "")
# print(lowcase_text)

# Create a list of words
split_text = lowcase_text.split(" ")
# print(split_text)

# Count the number of words
words_number = len(split_text)
# print(words_number)

# Prompt a letter from a user
input_letter = input("Please, enter a letter: ").lower()

# While input is not a latin letter, keep prompting
while input_letter not in alphabet:
    input_letter = input("Please, enter a letter: ").lower()

# Count number of words, starting with the input letter
counter = 0
for i in split_text:
    if i[0] == input_letter:
        counter += 1
# print(counter)

# Count the percentage of words, starting with the input letter in the text
percentage = (counter / words_number) * 100
print(f"Percentage of words, starting with the input letter in the text is {round(percentage, 2)}%.")

# Find the shortest word in the text
shortest_word = min(split_text, key=len)
print(f"The shortest word in the text is '{shortest_word}'.")

# Find the letter with which the maximum number of words start
# Create a list of first letters of words in the text
words_alpha = []
for i in split_text:
    words_alpha.append(i[0])
# print(words_alpha)

# Create a dictionary of letters and their number
max_letter_dict = {}
for i in alphabet:
    max_letter_dict.update({i: words_alpha.count(i)})
# print(max_letter_dict)

# Find the most common first letter
maxim_encounters = max(max_letter_dict.values())
frequent_letter = None
for letter, number in max_letter_dict.items():
    if number == maxim_encounters:
        frequent_letter = letter
print(f"The most common first letter in the text is '{frequent_letter}'.")

# Delete all even words from the text
# if i in range(words_number):


# Replace the first and last words
given_text = given_text.split(" ")
given_text[0], given_text[-1] = given_text[-1], given_text[0]
given_text = " ".join(given_text)
print(given_text)