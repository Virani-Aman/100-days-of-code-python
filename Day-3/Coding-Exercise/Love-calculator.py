print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

names_combined = name1 + name2
names = names_combined.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
true = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
love = l + o + v + e

true = str(true)
love = str(love)

score = true + love

score = int(score)

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")