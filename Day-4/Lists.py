#So we kmow that variable is a place where we can store a piece of data
#but sometimes we need to store multiple pieces of data sometimes even in a organised manner 
#for that we have lists, we can use lists to store multiple pieces of data in a organised well managed way
#For example lets say i am going on a trip to Netherlands and i gotta pack my bag for the trip.
#So i am gonna make a list of what all do i need to take like this -

things_to_take = ["Toothbrush", "Toothpaste", "Facewash", "Medicines", "Charger", "My Walllet", 
                  "Passport", "Visa", "3 Shirts", "3 T-Shirts", "3 Chinos", "3 Jeans", 
                  "10 Handkercheif", "5 PJ", "Laptop", "Laptop charger", "A pen", "Journal"]

# Now i have made a list of the things that i will take on the trip 
# now lets say i wanna know what the first thing is for that i will need to print it so i will print the first thing in the list like this

print(things_to_take[0])

#Now i used 0 beacause we know that we start counting from 0 in python

#now if we want to change something in a list we can change the list like this

#lets say i wanna change the amout of shirts from 3 to 2 so to do that i can basically change it like this

things_to_take[8] = "2 Shirts"
print(things_to_take)

#now lets say i wanna add my go pro to the list so to do that i ca just use the append function
#append function adds a single item to the list 
#it can be used like this

things_to_take.append("GoPro")

print(things_to_take)

#Now lets say i wanna add multiple things not just a single item to the list 
#to do that we can use the extend function like this 

things_to_take.extend(["The Subtle art of not giving a fuck book", "The Psychology of money book", "DO EPIC SHIT book"])
print(things_to_take)

# now lets say i want to remove the do epic shit book to do that i will just use the remove function like this 

things_to_take.remove("DO EPIC SHIT book")
print(things_to_take)

# Now theres a thing called nested lists 
# they can be used to lets say you are listing the members of a club but you want to give free drinks to women so while listing you make two different list but you also want them to be under the members_of_club variable 
#to do that we use nested list like this -

members_of_club_men = ["Mike", "Harvey", "Louis", "Robert", "Alex", "Aman"]
members_of_club_women = ["Rachel", "Donna", "Katrina", "Samantha"]

members_of_club = [members_of_club_men, members_of_club_women]

print(members_of_club)

# now lets say you wanted to know the first member of the club who is a man 
#we can just use the print command like this for it -
print(members_of_club[0][0])
# first 0 for the list 1 as python takes 0 as 1 and the other 0 for the first name again.
