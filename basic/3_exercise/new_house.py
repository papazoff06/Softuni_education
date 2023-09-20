flower = input()
flower_count = int(input())
budget = int(input())

Roses_price = 5
Dahlias_price = 3.80
Tulips_price = 2.80
Narcissus_price = 3
Gladiolus_price = 2.50

discount = 0
price = 0


if flower == 'Roses':
    price = Roses_price
    if flower_count > 80:
        discount = 0.10
elif flower == 'Dahlias':
    price = Dahlias_price
    if flower_count > 90:
        discount = 0.15
elif flower == 'Tulips':
    price = Tulips_price
    if flower_count > 80:
        discount = 0.15
elif flower == 'Narcissus':
    price = Narcissus_price
    if flower_count < 120:
        discount = - 0.15
elif flower == 'Gladiolus':
    price = Gladiolus_price
    if flower_count < 80:
        discount = - 0.20
final_price = flower_count * price * (1 - discount)

if final_price <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flower} and {budget - final_price:.2f} leva left.")
else:
    print(f'Not enough money, you need {final_price - budget:.2f} leva more.')



