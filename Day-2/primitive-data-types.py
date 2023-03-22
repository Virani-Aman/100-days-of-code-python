# Before we start we will learn a command called type command,
# so this command can be used to find the type of a data type
# it can be written like this -
type("Aman")


# So there are multiple primitive data types in python here is a list of them

# 1) String
# 2) Integer
# 3) Float
# 4) Boolean


# String
# String are written in between of two inverted commas (") like this
"Aman"
# Strings are used for characters and not for numbers,
# if numbers are used in strings the computer will treat them like some character thats a symbol

# Integer
# Integers are not written in between of two inverted commas or in between of anything.
# Integers are basically all numbers other then numbers with a decimal point
# Integers are written like this -
integers_example = 1217626
print(type(integers_example))

# Float
# Float are just integers but with a decibel point
# FLoats can be written like this -
float_example = 123.123
print(type(float_example))


# We are also going to cover one more thing and that is Type conversion
# So type conversion is the conversion between two datatypes like from string to integers or integers to float
# type conversion can be dome by a few commands such as

# str() (String conversion)
# int() (Integer conversion)
# float() (Float conversion)

# So basically its is very easy to convert between two datatypes using this commands
# Lets try to convert some of the datatypes

# String - Integer and vise versa
# things to know about this conversion that only a number in a string can be converted to a integer
# even if there is one character which is not a natural number then it will not be converted

# lets start -

number_in_string = "123"

number_in_integer = int(number_in_string)
print(type(number_in_integer))

number_in_string = str(number_in_integer)
print(type(number_in_string))

# conversion of string to float is also same as conversion of string to integer

# Conversion of integer to float
# just there is one thing to know about this conversion that is even if you dont add a decimal in the number the computer will add it automatically

number_in_float = float(number_in_integer)
print(type(number_in_float))
