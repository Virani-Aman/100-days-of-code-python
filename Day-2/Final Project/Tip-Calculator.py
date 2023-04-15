print("Welcome to the tip calculator")

total_bill = float(input("Please enter the total amount of the bill "))
tip_percentage = float(input("Please enter how much percentage do you to tip "))
bill_split = float(input("Please enter the number of people between whom you want to split the bill in "))

tip = (tip_percentage  / 100) * total_bill
tip = tip + total_bill

bill = tip / bill_split

final_bill = round(bill, 2)

print(f"Each person should pay {final_bill}")
