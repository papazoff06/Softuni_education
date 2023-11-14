from math import ceil
number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
maximum_bonus = 0
attended_lectures = 0
for i in range(number_of_the_students):
    count_of_attendances = int(input())
    total_bonus = count_of_attendances / number_of_the_lectures *(5 + additional_bonus)
    if total_bonus > maximum_bonus:
        maximum_bonus = total_bonus
        attended_lectures = count_of_attendances
print(f"Max Bonus: {ceil(maximum_bonus)}.")
print(f"The student has attended {attended_lectures} lectures.")

