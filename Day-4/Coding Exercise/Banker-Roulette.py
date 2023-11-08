names_string = input("Please enter the names. ")

names = names_string.split(", ")

names_number = len(names)

import random
names_number = names_number + 1
random_number = random.randint(0, names_number)

random_name = names[random_number]

print(f"{random_name} is going to buy the meal today!")