numbers = input().split(', ')
positive = ', '.join([number for number in numbers if int(number) >= 0])
negative = ', '.join([number for number in numbers if int(number) < 0])
even = ', '.join([number for number in numbers if int(number) % 2 == 0])
odd = ', '.join([number for number in numbers if int(number) % 2 != 0])
print(f'Positive: {positive}')
print(f'Negative: {negative}')
print(f'Even: {even}')
print(f'Odd: {odd}')

# both of decisions are ok!

def select_positive_numbers(numbers):
    return ', '.join([i for i in numbers if int(i) >= 0])
def select_negative_numbers(numbers):
    return ', '.join([i for i in numbers if int(i) < 0])
def select_even_numbers(numbers):
    return ', '.join([i for i in numbers if int(i) % 2 == 0])
def select_odd_numbers(numbers):
    return ', '.join([i for i in numbers if int(i) % 2 != 0])
sequence_numbers = input().split(', ')
print(f'Positive: {select_positive_numbers(sequence_numbers)}')
print(f'Negative: {select_negative_numbers(sequence_numbers)}')
print(f'Even: {select_even_numbers(sequence_numbers)}')
print(f'Odd: {select_odd_numbers(sequence_numbers)}')



