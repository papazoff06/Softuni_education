command = input()
some_dict = {}
while command != 'no more time':
    new_command = command.split('->')
    username, contest, points = new_command[0], new_command[1], int(new_command[2])
    if username not in some_dict.items():
        some_dict[username] = {contest: points}
    else:
        if some_dict[username][contest] < points:
            some_dict[username][contest] = points
    command = input()
print(some_dict)
