power = (
    ("мільярд", "мільярди", "мільярдів"),
    ("мільйон", "мільйони", "мільйонів"),
    ("тисяча", "тисячі", "тисяч"),
    (" ", " ", "")
)

# Також ми можемо перевести це в словник з кортежами
ordinary_numbers = {
    0: "",
    1: (" один", " одна"),
    2: (" два", " дві"),
    3: " три",
    4: " чотири",
    5: " п'ять",
    6: " шість",
    7: " сім",
    8: " вісім",
    9: " дев'ять",
    10: " десять",
    11: " одинадцять",
    12: " дванадцать",
    13: " тринадцать",
    14: " чотирнадцать",
    15: " п'ятнадцять",
    16: " шістьнадцять",
    17: " сімнадцять",
    18: " вісімнадцять",
    19: " дев'ятнадцять",
}
decimal_numbers = {
    0: "",
    2: " двадцать",
    3: " тридцать",
    4: " сорок",
    5: " п'ядесят",
    6: " шісдесят",
    7: " сімдесят",
    8: " вісімдесят",
    9: " дев'яносто"
}
hundreds = {
    0: "",
    1: " сто",
    2: " двісті",
    3: " триста",
    4: " чотириста",
    5: " п'ятсот",
    6: " шістсот",
    7: " сімсот",
    8: " вісімсот",
    9: " дев'ятсот"
}
numbers_for_thousands = {
    0: "",
    1: " одна",
    2: " дві",
    3: " три",
    4: " чотири"
}

# В нас є окрема функція яка дозволяє розбити число на сотні, тисячі, мільйони і мільярди
def getGrades(number):
    grades = (
        number / 1000000000,
        number % 1000000000 / 1000000,
        number % 1000000 / 1000,
        number % 1000
    )
    return grades

# окремо винесли визначення роду числа (вийняток для одиниці та двійки)
def getNumberForm(number, grade):
    if grade == 2 and type(ordinary_numbers[number]) != str:
        return ordinary_numbers[number][1]
    elif type(ordinary_numbers[number]) != str:
        return ordinary_numbers[number][0]

    return ordinary_numbers[number]

# отримуємо назви степенів
def getPower(remainderTen, i):
    if remainderTen == 1:
        return " {} ".format(power[i][0])
    elif remainderTen in (2, 3, 4):
        return " {} ".format(power[i][1])
    elif remainderTen in (0, 5, 6, 7, 8, 9, 10):
        return " {} ".format(power[i][2])
    return ""      

# перетворюємо число в стрічку
def getStringNumber(number):
    number = float(number)
    output = ""

    i = 0
    # проходимо циклом по розрядах
    for grade in getGrades(number):
        grade = int(grade)

        # якщо отримуємо 0 переходимо до наступного розряду
        if grade == 0:
            i+=1
            continue

        divHundred = int(grade / 100)
        remainderTen = int(grade % 10)
        remainderHundred = int(grade % 100)
        divRHTen = int(remainderHundred / 10)

        # обробляємо сотні
        if grade != 0 and divHundred != 0:
            output += hundreds[divHundred]

        # обробляємо десятки і одиниці
        if remainderHundred and divRHTen != 1:
            output += decimal_numbers[divRHTen]
        output += getNumberForm(remainderTen, i)

        # вийняток з числами від 10 до 19
        if remainderHundred >= 10 and remainderHundred <= 19:
            output += " {} ".format(power[i][2])
        else:
            output += getPower(remainderTen, i)
        i+=1

    return output.strip()

# також виводимо через assert повідомлення що щось пішло не так
number = input("Введіть число від 1 до : 2 147 483 647 ")
assert int(number), "Ви ввели не число. Введіть число: "

output = getStringNumber(number)  
print(output)