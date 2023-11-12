for number in range(1, 100 + 1):
    number_3 = number % 3
    number_5 = number % 5
    if number_3 == 0 and number_5 == 0:
        print("FizzBuzz")
    elif number_3 == 0 and number_5 != 0:
        print("Fizz")
    elif number_5 == 0 and number_3 != 0:
        print("Buzz")
    else:
        print(number)