print("Welcome to the tip calculator.")
total_bill = float(input("What was the total? "))
number_people = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_bill_tip = tip_percentage/100 * total_bill
total_bill_tip = total_bill_tip / number_people

total_bill_split = total_bill / number_people
total_bill = total_bill_split + total_bill_tip

print(f"Each person should pay: ${total_bill}")