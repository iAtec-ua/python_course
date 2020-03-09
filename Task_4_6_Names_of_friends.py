# The script shows full name of participants only for friends and short names for strangers

# Create a dictionary with full name of friends
friends = {
    "John": "Connor",
    "Sarah": "Connor",
    "Luke": "Skywalker",
    "Dart": "Vader",
    "Bill": "Clinton",
    "Monica": "Levinski"
}

# Prompt user to enter their name
name_input = input("What is your name? ").capitalize()

# If the name is in the dictionary, say hello
if name_input in friends:
    print(f"How you doing, {name_input} {friends[name_input]}?")
# If not, say sorry
else:
    print("I am sorry, I don't know you!")