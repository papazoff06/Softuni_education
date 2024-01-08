command = input()
some_dict = {}
while command != 'Log out':
    current_command = command.split(': ')
    if current_command[0] == 'New follower':
        username = current_command[1]
        if username not in some_dict:
            some_dict[username] = {'likes': 0, 'comments': 0}

    elif current_command[0] == 'Like':
        username = current_command[1]
        count = int(current_command[2])
        if username not in some_dict:
            some_dict[username] = {'likes': count, 'comments': 0}
        else:
            some_dict[username]['likes'] = some_dict[username]['likes'] + count

    elif current_command[0] == 'Comment':
        username = current_command[1]
        if username not in some_dict:
            some_dict[username] = {'likes': 0,'comments': 1}
        else:
            some_dict[username]['comments'] = some_dict[username]['comments'] + 1
    elif current_command[0] == 'Blocked':
        username = current_command[1]
        if username in some_dict:
            del some_dict[username]
        else:
            print(f"{username} doesn't exist.")
    command = input()

print(f'{len(some_dict)} followers')
for key, value in some_dict.items():
    result = value['likes'] + value['comments']
    print(f"{key}: {result}")