student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height = total_height + height

number_of_students = 0
for num in student_heights:
    number_of_students = number_of_students + 1

average_height = total_height/number_of_students
average_height  = round(average_height)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")
