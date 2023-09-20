
baggage_over_20kg_price = float(input())
baggage_kg = float(input())
days_travel = int(input())
baggage_count = int(input())

price = 0

if baggage_kg < 10:
    price = baggage_over_20kg_price * 0.20
elif 10 <= baggage_kg <= 20:
    price = baggage_over_20kg_price / 2
elif baggage_kg > 20:
    price = baggage_over_20kg_price
if days_travel > 30:
    price *= 1.1
elif 7 <= days_travel <= 30:
    price *= 1.15
elif days_travel < 7:
    price *= 1.4
final_price = price * baggage_count
print(f" The total price of bags is: {final_price:.2f} lv. ")
