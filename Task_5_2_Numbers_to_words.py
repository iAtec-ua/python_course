# Script prompts a number from user and prints the number in words

#   Create libraries for all kind of numbers
ordinary_numbers = {
    "0": "",
    "1": " один",
    "2": " два",
    "3": " три",
    "4": " чотири",
    "5": " п'ять",
    "6": " шість",
    "7": " сім",
    "8": " вісім",
    "9": " дев'ять",
    "10": " десять",
    "11": " одинадцять",
    "12": " дванадцать",
    "13": " тринадцать",
    "14": " чотирнадцать",
    "15": " п'ятнадцять",
    "16": " шістьнадцять",
    "17": " сімнадцять",
    "18": " вісімнадцять",
    "19": " дев'ятнадцять",
}
decimal_numbers = {
    "0": "",
    "2": " двадцать",
    "3": " тридцать",
    "4": " сорок",
    "5": " п'ядесят",
    "6": " шісдесят",
    "7": " сімдесят",
    "8": " вісімдесят",
    "9": " дев'яносто"
}
hundreds = {
    "0": "",
    "1": " сто",
    "2": " двісті",
    "3": " триста",
    "4": " чотириста",
    "5": " п'ятсот",
    "6": " шістсот",
    "7": " сімсот",
    "8": " вісімсот",
    "9": " дев'ятсот"
}
numbers_for_thousands = {
    "0": "",
    "1": " одна",
    "2": " дві",
    "3": " три",
    "4": " чотири"
}


def user_prompt(msg):
    prompt_number = input(msg)
    if not prompt_number.isdigit():
        return user_prompt("Вы ввели не число. Введіть число: ")
    if int(prompt_number) in range(1, 9999):
        number_length = len(prompt_number)
        number_list = list(prompt_number)
        int_prompt_number = int(prompt_number)
        if int_prompt_number < 20:
            print(f"Ваша цифра:{ordinary_numbers[prompt_number]}!")
        elif int_prompt_number < 100:
            print(f"Ваша цифра:{decimal_numbers[number_list[0]]}{ordinary_numbers[number_list[1]]}!")
        elif int_prompt_number < 1000:
            if int(number_list[-2]) == 1:
                decimal_list = number_list[-2:]
                decimals = str("".join(decimal_list))
                print(f"Ваша цифра:{hundreds[number_list[0]]}{ordinary_numbers[decimals]}!")
            else:
                print(
                    f"Ваша цифра:{hundreds[number_list[0]]}{decimal_numbers[number_list[1]]}{ordinary_numbers[number_list[2]]}!")
        elif int_prompt_number < 10000:
            if int(number_list[0]) == 1:
                if int(number_list[-2]) == 1:
                    decimal_list = number_list[-2:]
                    decimals = str("".join(decimal_list))
                    print(
                        f"Ваша цифра:{numbers_for_thousands[number_list[0]]} тисяча{hundreds[number_list[1]]}{ordinary_numbers[decimals]}!")
                else:
                    print(
                        f"Ваша цифра:{numbers_for_thousands[number_list[0]]} тисяча{hundreds[number_list[1]]}{decimal_numbers[number_list[2]]}{ordinary_numbers[number_list[3]]}!")
            elif int(number_list[0]) in range(1, 5):
                if int(number_list[-2]) == 1:
                    decimal_list = number_list[-2:]
                    decimals = str("".join(decimal_list))
                    print(
                        f"Ваша цифра:{numbers_for_thousands[number_list[0]]} тисячі{hundreds[number_list[1]]}{ordinary_numbers[decimals]}!")
                else:
                    print(
                        f"Ваша цифра:{numbers_for_thousands[number_list[0]]} тисячі{hundreds[number_list[1]]}{decimal_numbers[number_list[2]]}{ordinary_numbers[number_list[3]]}!")
            else:
                if int(number_list[-2]) == 1:
                    decimal_list = number_list[-2:]
                    decimals = str("".join(decimal_list))
                    print(
                        f"Ваша цифра:{ordinary_numbers[number_list[0]]} тисяч{hundreds[number_list[1]]}{ordinary_numbers[decimals]}!")
                else:
                    print(
                        f"Ваша цифра:{ordinary_numbers[number_list[0]]} тисяч{hundreds[number_list[1]]}{decimal_numbers[number_list[2]]}{ordinary_numbers[number_list[3]]}!")
    else:
        return user_prompt("Ваше число менше 1 або більше 9999. Введіть число від 1 до 9999:")


print(user_prompt("Введіть число від 1 до 9999: "))