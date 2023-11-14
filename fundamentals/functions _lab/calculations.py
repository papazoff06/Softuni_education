operator = input()
first_number = int(input())
second_number = int(input())


def calculator_yes(operator, number_1, number_2):
    if operator == 'multiply':
        return number_1 * number_2
    elif operator == 'divide':
        return int(number_1 / number_2)
    elif operator == 'add':
        return number_1 + number_2
    elif operator == 'subtract':
        return number_1 - number_2


result = calculator_yes(operator, first_number, second_number)
print(result)
