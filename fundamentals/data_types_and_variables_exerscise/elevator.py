number_of_people = int(input())
capacity = int(input())
course = 0
while number_of_people > 0:
    number_of_people -= capacity
    course += 1
print(course)