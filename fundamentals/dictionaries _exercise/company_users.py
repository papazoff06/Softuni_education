command = input()
some_dict = {}
while command != 'End':
    sequence = command.split('->')
    company_name = sequence[0]
    employees_id = sequence[1]
    if company_name not in some_dict.keys():
        some_dict[company_name] = [employees_id]
    else:
        if employees_id in some_dict[company_name]:
            command = input()
            continue
        some_dict[company_name].append(employees_id)
    command = input()
for key, value in some_dict.items():
    print(key)
    for i in value:
        print(f"--{i}")
