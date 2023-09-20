high_limit_first_number = int(input())
high_limit_second_number = int(input())
high_limit_third_number = int(input())
first_digit = 0
second_digit = 0
third_digit = 0

for a in range(1, high_limit_first_number + 1):
    first_digit = a
    for b in range(1, high_limit_second_number + 1):
        second_digit = b
        for c in range(1, high_limit_third_number + 1):
            third_digit = c
            if first_digit % 2 == 0 and (second_digit == 2 or second_digit == 3 or second_digit == 5 or second_digit == 7) \
                    and third_digit % 2 == 0:
                print(f'{first_digit}{second_digit}{third_digit}')
