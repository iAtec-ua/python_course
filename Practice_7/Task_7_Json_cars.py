# The script processes a file containing a list of cars and their features

import json

# Open the file for reading and print it
file = open('Car_Model_List.json', 'r', encoding='utf-8')
cars = file.read()
# print(cars)

# Create a list of brands
cars_dict = json.loads(cars)
brands = []
for i in cars_dict:
    while i["Make"] not in brands:
        brands.append(i["Make"])

brands.sort()
brands = ", ".join(brands)
print(f"You can chose a brand of a car: {brands}!")

# Create a list of models of a given brand
models = []
user_brand = input("Please, enter a brand to get a list of models: ")
for i in cars_dict:
    if i["Make"] == user_brand:
        while i["Model"] not in models:
            models.append(i["Model"])

models.sort()
models = ", ".join(models)
print(f"Here is the list of available models of {user_brand}: {models}!")

# Print all info about a car by a given model
# car_by_model = []
# user_model = input("Please, enter a model to get all information about it: ")
# for i in cars_dict:
#    if i["Model"] == user_model:
#        while i not in car_by_model:
#            car_by_model.append(i)
#
# print(f"Here is the list of available models of {car_by_model}!")

# Search all models of a brand in a given period of time
user_brand_2 = input("Please, enter a brand: ")
beginning = int(input("Please, enter a year of the beginning of a period: "))
ending = int(input("Please, enter a year of the end of a period: "))

models = []
for i in cars_dict:
    if i["Make"] == user_brand:
        if i["Year"] in range(beginning, ending):
            while i["Model"] not in models:
                models.append(i["Model"])

models.sort()
models = ", ".join(models)
print(f"Here is the list of available models of {user_brand}: {models}!")
