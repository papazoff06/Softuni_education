price_room_for_one_person = 18.00
price_apartment = 25
price_president_apartment = 35


vacation_days = int(input())
kind_of_room = input()
feedback = input()


price_pur_night = 0

if kind_of_room == 'room for one person':
    price_pur_night = price_room_for_one_person

elif kind_of_room == 'apartment':
    if vacation_days < 10:
        price_pur_night = price_apartment
        price_pur_night *= 0.70
    elif 10 <= vacation_days <= 15:
        price_pur_night = price_apartment
        price_pur_night *= 0.65
    elif  15 < vacation_days:
        price_pur_night = price_apartment
        price_pur_night *= 0.50

elif kind_of_room == 'president apartment':
    if vacation_days < 10:
        price_pur_night = price_president_apartment
        price_pur_night *= 0.90
    elif 10 <= vacation_days <= 15:
        price_pur_night = price_president_apartment
        price_pur_night *= 0.85
    elif  15 < vacation_days:
        price_pur_night = price_president_apartment
        price_pur_night *= 0.80

vacation_price = (vacation_days - 1) * price_pur_night

if feedback == "positive":
    vacation_price *= 1.25
elif feedback == "negative":
    vacation_price *= 0.90

print(f'{vacation_price:.2f}')

