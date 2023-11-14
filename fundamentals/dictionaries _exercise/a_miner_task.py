resource = input()
some_dict = {}
while resource != 'stop':
    quantity = int(input())
    if resource not in some_dict:
        some_dict[resource] = 0
    some_dict[resource] += quantity

    resource = input()
for resource, quantity in some_dict.items():
    print(f'{resource} -> {quantity}')

