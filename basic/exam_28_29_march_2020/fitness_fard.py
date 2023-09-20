# •	Сумата, с която разполагаме - реално число в интервала [10.00…1000.00]
# •	Пол - символ ('m' за мъж и 'f' за жена)
# •	Възраст - цяло число в интервала [5…105]
# •	Спорт - текст (една от възможностите в таблицата)
our_sum = float(input())
gender = input()
age = int(input())
sport = input()
price = 0
if gender == 'm':
    if sport == 'Gym':
        price = 42
    elif sport == 'Boxing':
        price = 41
    elif sport == 'Yoga':
        price = 45
    elif sport =='Zumba':
        price = 34
    elif sport == 'Dances':
        price = 51
    elif sport == 'Pilates':
        price = 39
elif gender == 'f':
    if sport == 'Gym':
        price = 35
    elif sport == 'Boxing':
        price = 37
    elif sport == 'Yoga':
        price = 42
    elif sport =='Zumba':
        price = 31
    elif sport == 'Dances':
        price = 53
    elif sport == 'Pilates':
        price = 37
if age <= 19:
    price *= 0.80
if our_sum >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${price - our_sum:.2f} more.")

