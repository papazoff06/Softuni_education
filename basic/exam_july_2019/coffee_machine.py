drink = input()
sugar = input()
drinks_count = int(input())
price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.20
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60
elif drink == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

total_sum = drinks_count * price
if sugar == 'Without':
    total_sum *= 0.65
if drink == 'Espresso' and drinks_count >= 5:
    total_sum *= 0.75
if total_sum > 15:
    total_sum *= 0.80
print(f"You bought {drinks_count} cups of {drink} for {total_sum:.2f} lv.")


