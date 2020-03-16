# The script processes a file containing a list of cars and their features

import json

# Open the file for reading and print it
file = open('Car_Model_List.json', 'r', encoding='utf-8')
cars = file.read()
print(cars)

# Create a list of brands
cars_dict = json.loads(cars)
brands = []
for i in cars_dict:
    while i["Make"] not in brands:
        brands.append(i["Make"])

brands.sort()
brands = ", ".join(brands)
print(f"You can chose a brand of a car: {brands}")
