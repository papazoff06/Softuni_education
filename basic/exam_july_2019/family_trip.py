budget = float(input())
nights_count = int(input())
price_per_night = float(input())
percent_extra_expences = int(input())
extra_expences = budget * percent_extra_expences / 100

if nights_count > 7:
    price_per_night *= 0.95

final_sum = (nights_count * price_per_night) + extra_expences
if budget >= final_sum:
    print(f"Ivanovi will be left with {budget - final_sum:.2f} leva after vacation.")
else:
    print(f"{final_sum - budget:.2f} leva needed.")