# IF ELSE  statements are used to make a choice between multiple data 

#for example imagine you are given a job to code a machine that sells tickets at a amusmment park
#but there are rules for who can sit on one of the rides
#like height should 120cm and age should be 10+

#To code this you can use if else statements like this:

minimum_height = "120"
minimum_age = "10"

height = input("Please enter your Height in cm ")
age = input("Please enter your Age ")

if height >= minimum_height:
    if minimum_age  < age:
        print("You can ride the rollercoaster")
    else:
        print("Sorry you have to be 10 years old to ride the roller coaster")

else:
    print("Sorry your height is smaller then the required limit") 