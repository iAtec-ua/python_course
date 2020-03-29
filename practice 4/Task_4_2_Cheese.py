# Script calculates price of cheese with 50 gram steps up to 1 kilogram

# Prompt price of cheese
price = input("What is the price of the product? ")

# Check for ValueError
while True:
    try:
        float(price)
        for i in range(50, 1001, 50):
            step_price = (i * float(price)) / 1000
            print(f"The price of {i} grams of the product is ${round(step_price, 2)}.")
        break
    except ValueError:
        # Not a valid number
        print("You must enter an integer!")
        price = input("Please, enter a number: ")

    # price = float(price) / 1000
    # for i in range(50, 1001, 50):
    #     step_price = i * price
    #     print(f"The price of {i} grams of the product is ${round(step_price, 2)}.")
с