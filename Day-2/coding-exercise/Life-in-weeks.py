age = input("What is your current age?")

age = int(age)

remaining_age = 90 - age

remaining_weeks = remaining_age * 52

remaining_days = remaining_age * 365

remaining_months = remaining_age * 12

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left")