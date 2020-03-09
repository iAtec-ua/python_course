# Script prompts a number from user and prints the number in words

#   Create libraries for all kind of numbers
ordinary_numbers = {
    "0": "",
    "1": "один",
    "2": "два",
    "3": "три",
    "4": "чотири",
    "5": "п'ять",
    "6": "шість",
    "7": "сім",
    "8": "вісім",
    "9": "дев'ять",
    "10": "десять",
    "11": "одинадцять",
    "12": "дванадцать",
    "13": "тринадцать",
    "14": "чотирнадцать",
    "15": "п'ятнадцять",
    "16": "шістьнадцять",
    "17": "сімнадцять",
    "18": "вісімнадцять",
    "19": "дев'ятнадцять",
}
decimal_numbers = {
    "20": "двадцать",
    "30": "тридцать",
    "40": "сорок",
    "50": "п'ядесят",
    "60": "шісдесят",
    "70": "сімдесят",
    "80": "вісімдесят",
    "90": "дев'яносто"
}
hundreds = {
    "100": "сто",
    "200": "двісті",
    "300": "триста",
    "400": "чотириста",
    "500": "п'ятсот",
    "600": "шістсот",
    "700": "сімсот",
    "800": "вісімсот",
    "900": "деі'ятсот"
}
numbers_for_thousands = {
    "1": "одна",
    "2": "дві"
}

# Prompt user to enter a number
prompt_number = input("Введіть число (від 1 до 999999): ")

# Check for ValueError
while True:
    try:
        int(prompt_number)
    except ValueError:
        # Not a valid number
        print("Це має бути число!")
        prompt_number = input("Будь ласка, введіть ціле число від 1 до 999999: ")
    else:
        # No error; stop the loop
        break

number_length = len(prompt_number)
int_prompt_number = int(prompt_number)

if int_prompt_number <= 19:
    print("")