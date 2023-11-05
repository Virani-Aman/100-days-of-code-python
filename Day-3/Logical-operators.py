#so logical operators are used with if statements to make it more efficient
#basically they are used like this
 
#So there are 3 Logical Operators - 
#1) and
#2) or
#3) not

#and operator can be used when you need multiple conditions to be fullfiled to execute a task 
#for example it can be used like:
age = 14
height_in_cm = 170

if age >= 10 and height_in_cm >= 150:
    print("You are allowed enter")

# so here rather than us using a if statement and then embedding another if statement inside the first if statemnt we can just use this, 
# it makes the code more clear and efficient

# or operator is used when you have multiple conditions but all dont need to be fullfiled.
# for example it can be used like - 

answer = input("Please eneter yes if you want to participate in the competion ")

if answer == "yes" or answer == "YES" or answer == "Yes":
    print("You have been registered as a participent in the comeption")

#so rather than us writing multiple if statements we can just use this.

#not logical operator is used when you want only execute a command if somethings is not true (false)
#for example it can be used like this 
my_age = 15

if not my_age >= 18:
    print("Sorry you are not allowed to participate")

