command = input()

some_dict = {}
while '-' in command:
    phone_book = command.split('-')
    people = phone_book[0]
    phone = phone_book[1]
    if people not in some_dict.keys():
        some_dict[people] = phone
    some_dict[people] = phone
    command = input()
else:
    for i in range(int(command)):
        search_name = input()
        if search_name in some_dict.keys():
            print(f'{search_name} -> {some_dict[search_name]}')
        else:
            print(f'Contact {search_name} does not exist.')
