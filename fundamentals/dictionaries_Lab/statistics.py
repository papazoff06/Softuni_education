command = input()
my_dict = {}
while command != "statistics":
    items = command.split(': ')
    key = items[0]
    value = int(items[1])
    if key not in my_dict:
        my_dict[key] = 0
    my_dict[key] += value
    command = input()
print("Products in stock:")
for (key, value) in my_dict.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(my_dict)}')
print(f'Total Quantity: {sum(my_dict.values())}')