city_name = input()
kind_of_package = input()
vip = input()
vacation_days = int(input())
if vacation_days > 7:
    vacation_days -= 1
price_per_day = 0

if vacation_days < 1:
    print('Days must be positive number!')
else:
    if city_name == 'Bansko' or city_name == 'Borovets':
        if kind_of_package == 'withEquipment':
            price_per_day = 100
            if vip == 'yes':
                price_per_day *= 0.90
            else:
                price_per_day = price_per_day
            final_price = vacation_days * price_per_day
            print(f'The price is {final_price:.2f}lv! Have a nice time!')
        elif kind_of_package == 'noEquipment':
            price_per_day = 80
            if vip == 'yes':
                price_per_day *= 0.95
            else:
                price_per_day = price_per_day
            final_price = vacation_days * price_per_day
            print(f'The price is {final_price:.2f}lv! Have a nice time!')
    elif city_name == 'Varna' or city_name == 'Burgas':
        if kind_of_package == 'withBreakfast':
            price_per_day = 130
            if vip == 'yes':
                price_per_day *= 0.88
            else:
                price_per_day = price_per_day
            final_price = vacation_days * price_per_day
            print(f'The price is {final_price:.2f}lv! Have a nice time!')
        elif kind_of_package == 'noBreakfast':
            price_per_day = 100
            if vip == 'yes':
                price_per_day *= 0.93
            else:
                price_per_day = price_per_day
            final_price = vacation_days * price_per_day
            print(f'The price is {final_price:.2f}lv! Have a nice time!')
    else:
        print("Invalid input!")
