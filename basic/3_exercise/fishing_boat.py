budget = int(input())
season = input()
fishers_count = int(input())

spring_rent_price = 3000
summer_and_autumn_rent_price = 4200
winter_rent_price = 2600
discount = 0
extra_discount = 0
price = 0

if season == 'Spring':
    price = spring_rent_price
    if 1 <= fishers_count <= 6:
        discount = 0.10
    elif 7 <= fishers_count <= 11:
        discount = 0.15
    elif fishers_count >= 12:
        discount = 0.25
elif season == 'Summer':
    price = summer_and_autumn_rent_price
    if 1 <= fishers_count <= 6:
        discount = 0.10
    elif 7 <= fishers_count <= 11:
        discount = 0.15
    elif fishers_count >= 12:
        discount = 0.25
elif season == 'Autumn':
    price = summer_and_autumn_rent_price
    if 1 <= fishers_count <= 6:
        discount = 0.10
    elif 7 <= fishers_count <= 11:
        discount = 0.15
    elif fishers_count >= 12:
        discount = 0.25
elif season == 'Winter':
    price = winter_rent_price
    if 1 <= fishers_count <= 6:
        discount = 0.10
    elif 7 <= fishers_count <= 11:
        discount = 0.15
    elif fishers_count >= 12:
        discount = 0.25


if season == 'Spring' or season == 'Summer' or season == 'Winter':
    if fishers_count % 2 == 0:
        extra_discount = 0.05
final_price = (price * (1 - discount)) * (1 - extra_discount)
if budget >= final_price:
    print(f"Yes! You have {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva.")


