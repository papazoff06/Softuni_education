import sys

max_num = - sys.maxsize
sum_numbers = 0

n = int(input())
for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num
    rest_sum = sum_numbers - max_num
if max_num == rest_sum:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = max_num - rest_sum
    print('No')
    print(f'Diff = {abs(diff)}')
