import math
fan_name = input()
budget = float(input())
beer_bottles_count = int(input())
chips_count = int(input())

birra_price = 1.20
chips_price = (beer_bottles_count * birra_price) * 0.45


expences = (beer_bottles_count * birra_price) + math.ceil(chips_count * chips_price)

if budget >= expences:
    print(f"{fan_name} bought a snack and has {budget - expences:.2f} leva left.")
else:
    print(f"{fan_name} needs {expences - budget:.2f} more leva!")