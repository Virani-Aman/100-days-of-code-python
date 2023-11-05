# So today we are going to learn number mainpulation

# in number manipulation we are going to learn -
# 1) Floor Division
# 2) Easy was to use arithmetic operators

# Let's start with floor division

# So Floor Division is made up of two things first is the round command and second is the division operator.

# so lets first start with rounding

# lets take 2.66666
# In this case we are going to round the number to the nearest integer, but how do we do it

# to perform this task we can use the round command like this:

print(round(2.666666))


# now what if we want to round the number to the nearest second decimal point
# to do that we can write the place value of the decimal point like this -

print(round(2.666666, 2))

# Now we know division so we are going to skip that part

# So you can use the floor division to divide the number as well as round it to the nearest integer, like this:

print(7 // 2)

# and you will notice that this will return the number in integer data type

# Let's move on to shortcuts for arithmetic operations

# Let's start with addition

# so let us think that this is a game and the intial score of the user is 0
# so that will be:

score = 0

# and the user scores 1 point so either then writing:

# score = score + 1

# We can just write

score += 1

print(score)


# Now let's start with subtraction
# so let us think that this is a game and the intial score of the user is 0

# and the user loses 1 point

# we can do the subtarction like this then

score -= 1

print(score)


# and this works for all the basic operators here are their commands

# 1) score += 1 (Addition)
# 2) score -= 1 (Subtraction)
# 3) score /= 2 (Division)
# 4) score *= 2 (Multiplication)
