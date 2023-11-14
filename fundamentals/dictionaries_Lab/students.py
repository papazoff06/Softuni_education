command = input()
my_dict = []
while ':' in command:
    name, ID, course = command.split(':')
    my_dict.append({'name': name, 'ID': ID, 'course': course})
    command = input()

else:
    searched_word = command
for student in my_dict:
    if searched_word.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")


