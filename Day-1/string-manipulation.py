# String manipulation is the addition of two strings in different was like this

print("Hello " + "World!")

# Or you can use variables in the print command
# BTW variables are a place where you can store some data

a = "Hello "
b = "World!"

print(a + b)

# F Strings 

#  So normally when you have to print something and you wrote some text and then added a plus sign and then 
# convert the dattatype to string if it was a integer and then it would get printed
# So to solve this problem we can use f strings instead like this

score  = 3.56
# the old way of printing

print("Your score is " + str(score))

# the new way of printing

print(f"Your score is {score}")