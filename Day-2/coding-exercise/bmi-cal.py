height = input("Please enter your height in meters: ")
weight = input("Please enter your weight in Kg: ")

height = float(height)
weight = float(weight)

bmi = weight / (height ** 2)

bmi = round(bmi)

print(bmi)