vacation_days = int(input())
kind_of_room = input()
feedback = input()

room_for_one_per_night_price = 18
apartment = 25
president_apartment = 35

price = 0

if kind_of_room == 'room for one person':
    price = room_for_one_per_night_price

elif kind_of_room == 'apartment':
    if 10 > vacation_days:
        price = apartment * 0.70
    elif 10 <= vacation_days <= 15:
        price = apartment * 0.65
    elif vacation_days > 15:
        price = apartment * 0.5

elif kind_of_room == 'president apartment':
    if 10 > vacation_days:
        price = president_apartment * 0.90
    elif 10 <= vacation_days <= 15:
        price = president_apartment * 0.85
    elif vacation_days > 15:
        price = president_apartment * 0.80

final_price = (vacation_days - 1) * price
if feedback == 'positive':
    final_price *= 1.25
elif feedback == 'negative':
    final_price *= 0.90
print(f'{final_price:.2f}')
