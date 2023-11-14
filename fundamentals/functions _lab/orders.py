kind_of_drink = input()
count_of_drinks = float(input())


def total_price(drink, quantity):
    if drink == 'coffee':
        return f'{1.50 * quantity:.2f}'
    elif drink == 'water':
        return f'{1 * quantity:.2f}'
    elif drink == 'coke':
        return f'{1.40 * quantity:.2f}'
    elif drink == 'snacks':
        return f'{2 * quantity:.2f}'


print(total_price(kind_of_drink, count_of_drinks))