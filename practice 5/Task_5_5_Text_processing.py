# The script processes a given text in different ways

# Import string to work with alphabet
import string

alphabet = list(string.ascii_lowercase)

# The given text
given_text = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"""

# Count the number of sentences
lowcase_text = given_text.lower()
sentences_end = [".", "?", "!"]

number_of_sentences = lowcase_text.count(".") + lowcase_text.count("?") + lowcase_text.count("!")
print(f"Number of sentences in the text is {number_of_sentences}.")

# Count the number of the word 'quis' in the text
quis_count = lowcase_text.count("quis")
print(f"The word 'quis' appears {quis_count} times in the text.")

# Count the number of all symbols in the text
number_of_all_symbols = len(lowcase_text)
print(f"Number of all symbols in the text is {number_of_all_symbols}.")

# Count the number of sentences in the text without spaces
no_spaces_text = lowcase_text.replace(" ", "")
number_of_symbols_without_spaces = len(no_spaces_text)
print(f"Number of symbols in the text (except spaces) is {number_of_symbols_without_spaces}.")

# Print the text before the 120th symbol and add '...' in the end
# If the 120th symbol is a part of a word, delete the word
abridged_text_list = list(given_text[0: 119])
while abridged_text_list[-1] in alphabet:
    abridged_text_list.pop(-1)
abridged_text = "".join(abridged_text_list)
print(f"The text before the 120 symbol is '{abridged_text}...'")
