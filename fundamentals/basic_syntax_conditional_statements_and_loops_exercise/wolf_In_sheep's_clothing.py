ships = input()
ship_number = 0

my_list = ships.split(", ")
if my_list[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for index in range(- 1, - len(my_list) - 1, - 1):
        if my_list[index] == 'sheep':
            ship_number += 1
        else:
            break
    print(f'Oi! Sheep number {ship_number}! You are about to be eaten by a wolf!')




