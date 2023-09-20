number = int(input())
is_current_biger_than_number = False
current = 1

for row in range(1, number + 1):
    for column in range(1, row + 1):
        if current > number:
            is_current_biger_than_number = True
            break
        print(f'{current}', end=' ')
        current += 1

    if is_current_biger_than_number:
        break
    print()
