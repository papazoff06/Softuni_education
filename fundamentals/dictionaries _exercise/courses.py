command = input()
some_dict = {}
while command != 'end':
    courses = command.split(' : ')
    course_name = courses[0]
    student_name = courses[1]
    if course_name not in some_dict.keys():
        some_dict[course_name] = [student_name]
    else:
        some_dict[course_name].append(student_name)
    command = input()
for course, name in some_dict.items():
    print(f"{course}: {len(name)}")
    for i in name:
        print(f"-- {i}")