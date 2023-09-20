# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
# •	Втори ред - пакет за филм - текст  с възможности "Drink", "Popcorn" или "Menu"
# •	Трети ред - брой билети - цяло число в интервала [1… 30]
movie = input()
package = input()
count_of_ticket = int(input())
price = 0
if movie == 'John Wick':
    if package == 'Drink':
        price = 12
    elif package == 'Popcorn':
        price = 15
    elif package == 'Menu':
        price = 19
elif movie == 'Star Wars':
    if package == 'Drink':
        price = 18
    elif package == 'Popcorn':
        price = 25
    elif package == 'Menu':
        price = 30
elif movie == 'Jumanji':
    if package == 'Drink':
        price = 9
    elif package == 'Popcorn':
        price = 11
    elif package == 'Menu':
        price = 14
final_price = price * count_of_ticket
if movie == 'Star Wars':
    if count_of_ticket >= 4:
        final_price *= 0.70
if movie == 'Jumanji':
    if count_of_ticket == 2:
        final_price *= 0.85
print(f"Your bill is {final_price:.2f} leva.")