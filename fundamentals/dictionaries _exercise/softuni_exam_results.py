command = input()
language_length = {}
name_points = {}
while command != 'exam finished':
    sequence = command.split("-")
    username = sequence[0]
    language = sequence[1]
    if language == 'banned':
        del name_points[username]
        break

    points = int(sequence[2])
    if username not in name_points.keys():
        language_length[language] = [language]
        name_points[username] = points
    else:
        language_length[language].append(language)
        if name_points[username] > points:
            name_points[username] = name_points[username]
        else:
            name_points[username] = points
            language_length[language].append(language)

    command = input()
print('Results:', end='')
for user, points in name_points.items():
    print(f"\n{user} | {points}")
print('Submissions:', end='')
for name, sub in language_length.items():
    submissions = len(sub)
    print(f"\n{name} - {submissions}")