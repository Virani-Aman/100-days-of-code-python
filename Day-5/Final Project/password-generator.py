import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

#Letters
random_letter_final = []
for n in range(1, nr_letters + 1):
    random_letter_number = random.randint(0, 51)
    random_letter = letters[random_letter_number]
    random_letter_final.append(random_letter)

#Number
random_number_final = []
for n in range(1, nr_numbers + 1):
    random_number = random.randint(0, 9)
    random_number = numbers[random_number]
    random_number_final.append(random_number)


#Symbols
random_symbol_final = []
for n in range(1, nr_symbols + 1):
    random_symbol = random.randint(0, 8)
    random_symbol = symbols[random_symbol]
    random_symbol_final.append(random_symbol)


#Adding the list together
password_list.extend(random_symbol_final)
password_list.extend(random_letter_final)
password_list.extend(random_number_final)

#shuffling all characters
random.shuffle(password_list)

#Converting to string
password = ""
for password_character in password_list:
    password = password + password_character

#DONE
print(password)