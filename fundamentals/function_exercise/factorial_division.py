def factorial_number(num):
    for factorial_num in range(1, num):
        num *= factorial_num
    return num



number_1 = int(input())
number_2 = int(input())
first_factorial_num = factorial_number(number_1)
second_factorial_num = factorial_number(number_2)
result = first_factorial_num / second_factorial_num
print(f'{result:.2f}')