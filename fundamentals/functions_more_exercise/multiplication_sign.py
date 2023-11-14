def multiplication(a: list):
    minus = 0
    for number in a:
        if number == 0:
            return 'zero'
        if number < 0:
            minus += 1
    if minus % 2 != 0:
        return "negative"
    else:
        return 'positive'


first_number = int(input())
second_number = int(input())
third_number = int(input())
my_list_a = [first_number, second_number, third_number]
print(multiplication(my_list_a))