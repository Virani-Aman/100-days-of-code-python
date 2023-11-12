target = int(input()) 

final_number = 0
for number in range(1, target + 1):
    number_remainder = number % 2
    if number_remainder == 0:
        final_number = final_number + number

print(final_number)