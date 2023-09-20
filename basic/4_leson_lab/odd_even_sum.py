numbers_count = int(input())
evan_sum = 0
odd_sum = 0

for numbers in range(numbers_count):
    current_number = int(input())
    if numbers % 2 == 0:
        evan_sum = current_number + evan_sum
    else:
        odd_sum += current_number

if evan_sum == odd_sum:
    print('Yes')
    print(f'Sum = {evan_sum}')
else:
    diff = abs(evan_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')







