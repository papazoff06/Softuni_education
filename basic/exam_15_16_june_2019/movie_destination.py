# От конзолата се четат 4 реда:
# 1.	Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
# 2.	Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
# 3.	Сезон – текст, с възможности "Summer" и "Winter"
# 4.	Брой дни  – цяло число в диапазона [1… 40]
budget = float(input())
destination = input()
season = input()
price = 0
count_of_days = int(input())
if destination == 'Dubai':
    if season == 'Winter':
        price = 45000
    elif season == 'Summer':
        price = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        price = 17000
    elif season == 'Summer':
        price = 12500
elif destination == 'London':
    if season == 'Winter':
        price = 24000
    elif season == 'Summer':
        price = 20250
final_price = count_of_days * price
if destination == 'Dubai':
    final_price *= 0.70
if destination == 'Sofia':
    final_price *= 1.25
if budget >= final_price:
    print(f"The budget for the movie is enough! We have {budget - final_price:.2f} leva left!")
else:
    print(f"The director needs {final_price - budget:.2f} leva more!")
