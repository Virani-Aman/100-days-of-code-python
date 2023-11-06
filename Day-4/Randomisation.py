#So randomisation is what?
#its basically something that is not predictable.
#for example if you roll a dice yes you can predict that it will be between 1-6 but you dont know what number exactly.

#So randomisation is a natural phenomen in life
#But to randomize things in a computer is very hard as computers basically are devices which do things based on commands and on logic.
#for example i know that if i select a file and press delete button on my keyboard the file will be delted 

#So to randomize things in a computer we use a Pseudo Random Number Generator (PRNG) (you dont need to learn this, its not important but its good to know about)
#So making our own Pseudo Random Number Generator (PRNG) would take us months so we use a module which is already provided in python called random

#Module are basically pieces of code which do a specific task and are kept in another file 
#like if a company is making a car some people work on the engine some on the body of the car and some on the interior like that modules are basically different teams which have different parts of code.

#So to use the random module we first need to import it like this 
import random

# now we have imported the random module so now we can start with the randomisation 
# so now lets say we want to get a random integer to get a output of a random integer we can just just the randint function, like this -

random_integer = random.randint(1, 10)
print(random_integer)

#so basically what is happening is when we write random.randint(1, 10) the program first reads random and then goes to the random module and then it reads randint(1, 10) where 1, 10 is basically the range of it then it finds the randint functions reads the code and then comes back here and executes it

# we can get a output of random float by using the random.random() but the problem is this will only generate a random float number between 0 and 1 
# but then we can just multiple the output with with 5 to increase its range.
# we can use the command like this - 

#random float between 0 and 1 (1 will not be given as a output ever)
random_float = random.random()
print(random_float)

#random float between 0 and 10 (leaving 10)
random_float = random.random()
random_float = random_float * 10
print(random_float)