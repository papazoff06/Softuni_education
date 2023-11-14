number_of_commands  = int(input())
some_dict = {}
for i in range(number_of_commands):
    users_data = input().split()
    if users_data[0] == 'register':
        username = users_data[1]
        license_plate_number = users_data[2]
        if username not in some_dict.keys():
            some_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {some_dict[username]}")
    elif users_data[0] == 'unregister':
        username = users_data[1]
        if username not in some_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            del some_dict[username]
            print(f"{username} unregistered successfully")
for all_users, plates in some_dict.items():
    print(f"{all_users} => {plates}")
