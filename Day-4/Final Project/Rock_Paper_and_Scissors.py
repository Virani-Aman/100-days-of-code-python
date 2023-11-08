import random
print("To choose ROCK enter 1 for PAPER enter 2 and for SCISSORS enter 3")

choice = input()

if choice == "1":
    print("               | |") 
    print(" _ __ ___   ___| | __")
    print("| '__/ _ \ / __| |/ /")
    print("| | | (_) | (__|   <")
    print("|_|  \___/ \___|_|\_\ ")
elif choice == "2":
    print(" _ __   __ _ _ __   ___ _ __")
    print("| '_ \ / _` | '_ \ / _ \ '__|")
    print("| |_) | (_| | |_) |  __/ |") 
    print("| .__/ \__,_| .__/ \___|_|")   
    print("| |         | |")              
    print("|_|         |_|")
else:
    print("          _                        ")
    print("         (_)                       ")
    print(" ___  ___ _ ___ ___  ___  _ __ ___ ")
    print("/ __|/ __| / __/ __|/ _ \| '__/ __|")
    print("\__ \ (__| \__ \__ \ (_) | |  \__ \ ")
    print("|___/\___|_|___/___/\___/|_|  |___/")

print("Computer chose:")
computer_choice = random.randint(1, 3)
computer_choice = str(computer_choice)
if computer_choice == "1":
    print("               | |")
    print(" _ __ ___   ___| | __")
    print("| '__/ _ \ / __| |/ /")
    print("| | | (_) | (__|   <")
    print("|_|  \___/ \___|_|\_\ ")
elif computer_choice == "2":
    print(" _ __   __ _ _ __   ___ _ __")
    print("| '_ \ / _` | '_ \ / _ \ '__|")
    print("| |_) | (_| | |_) |  __/ |")
    print("| .__/ \__,_| .__/ \___|_|")
    print("| |         | |")
    print("|_|         |_|")
else:
    print("          _                        ")
    print("         (_)                       ")
    print(" ___  ___ _ ___ ___  ___  _ __ ___ ")
    print("/ __|/ __| / __/ __|/ _ \| '__/ __|")
    print("\__ \ (__| \__ \__ \ (_) | |  \__ \ ")
    print("|___/\___|_|___/___/\___/|_|  |___/")

if choice == "1":
    if computer_choice == "1":
        print("TIE")
    if computer_choice == "2":
        print("YOU WIN")
    elif computer_choice == "3":
        print("YOU LOSE")
elif choice == "2":
    if computer_choice == "1":
        print("YOU WIN")
    if computer_choice == "2":
       print("TIE")
    elif computer_choice == "3":
        print("YOU LOSE")
else:
    if computer_choice == "1":
        print("YOU LOSE")
    if computer_choice == "2":
        print("YOU WIN")
    elif computer_choice == "3":
        print("TIE")