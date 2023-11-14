command = input()
some_dict = {}
while command != 'Lumpawaroo':
    if '|' in command:
        side_1 = command.split('|')
        force_side = side_1[0]
        force_user = side_1[1]
        if force_side and force_user not in some_dict.items():
            some_dict[force_side] = [force_user]
        if force_user not in some_dict.keys():
            some_dict[force_side].append(force_user)
        else:
            continue
    if '->' in command:
        side_1 = command.split('->')
        force_user = side_1[0]
        force_side = side_1[1]
        if force_user in some_dict.keys():
            some_dict[force_side] = [force_user]
        if force_user not in some_dict.items():
            some_dict[force_user] = [force_side]
        if force_side and force_user not in some_dict.items():
            some_dict[force_user] = [force_side]
            print(f"{force_user} joins the {force_side} side!")
    command = input()
for key, value in some_dict.items():
    print(f"Side: {key}, Members: {len(value)}")
    for i in value:
        if len(value) == 0:
            continue
        print(f"! {i}")