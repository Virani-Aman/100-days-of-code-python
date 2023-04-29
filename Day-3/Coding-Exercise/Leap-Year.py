year = int(input("Which year do you want to check? "))

year_4 = year % 4
year_100 = year % 100
year_400 = year % 400

if year_4 == 0:
    if year_100 == 0:
        if year_400 == 0:
            print("Leap year.")
    if year_100 != 0:
        print("Leap year.")
    if year_100 == 0:
        if year_400 != 0:
            print("Not leap year.")
else:
    print("Not leap year.")
    