import string

alphabet = list(string.ascii_lowercase)

given_text = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"""

# Гарною практикою є розділення коду з різною логікою порожньою стрічкою
# Це дозволяє легше сприймати код

# все інше чудово, окрім останнього завдання
lowcase_text = given_text.lower()
sentences_end = [".", "?", "!"]
counter = 0

for i in sentences_end:
    counter
number_of_sentences = lowcase_text.count(".") + lowcase_text.count("?") + lowcase_text.count("!")
print(f"Number of sentences in the text is {number_of_sentences}.")

quis_count = lowcase_text.count("quis")
print(f"The word 'quis' appears {quis_count} times in the text.")

number_of_all_symbols = len(lowcase_text)
print(f"Number of all symbols in the text is {number_of_all_symbols}.")

no_spaces_text = lowcase_text.replace(" ", "")
number_of_symbols_without_spaces = len(no_spaces_text)
print(f"Number of symbols in the text (except spaces) is {number_of_symbols_without_spaces}.")

#Вивести на екран перші 120 символів та додати «...»після останнього слова. 
# Необхідно видалити останнє слово, якщо воно не буде виведено повністю

# Функція reverse дещо недоцільна
# Адже нам не треба розвертати 120 символів
text_list = list(given_text)
sliced_list = text_list[0: 120]
rev_sliced_list = sliced_list.reverse()

print(f"The text before the 120 symbol is {rev_sliced_list}...")
