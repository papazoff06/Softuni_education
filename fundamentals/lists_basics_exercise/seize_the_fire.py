fires = input().split('#')
water = int(input())
effort = 0
total_fire = 0
put_out_cells = []
print('Cells:')
for i in fires:
    symbol = i.split(' = ')
    fire_type = symbol[0]
    fire_level = int(symbol[1])
    is_valid = False
    if water < fire_level:
        continue
    if fire_type == 'High':
        if 81 <= fire_level <= 125:
            is_valid = True
    elif fire_type == 'Medium':
        if 51 <= fire_level <= 80:
            is_valid = True
    elif fire_type == 'Low':
        if 1 <= fire_level <= 50:
            is_valid = True
    if is_valid:
        put_out_cells.append(fire_level)
        water -= fire_level
        effort += fire_level * 0.25
        total_fire += fire_level


for cells in put_out_cells:
    print(f' - {cells}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

