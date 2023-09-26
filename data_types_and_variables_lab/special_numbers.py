number = int(input())
numbers_sum = 0
for i in range(1, number + 1):
    current_number = str(i)
    for j in current_number:
        numbers_sum += int(j)
    if numbers_sum == 5 or numbers_sum == 7 or numbers_sum == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
    numbers_sum = 0
