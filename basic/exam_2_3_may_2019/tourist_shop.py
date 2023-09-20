# От конзолата се чете:
# •	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# •	След това поредица от два реда (до получаване на команда "Stop" или при заявка за купуване на продукт, чиято стойност е по-висока от наличния бюджет) :
# o	Име на продукта – текст
# o	Цена на продукта – реално число в интервала [1.00… 5000.00]
budget = float(input())
command = input()
leaving_budget = budget
counter = 0
while command != 'Stop':
    price = float(input())
    counter += 1
    if counter % 3 == 0:
        price *= 0.50
    budget -= price
    if budget < 0:
        print("You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
        break
    command = input()
if command == 'Stop':
    print(f"You bought {counter} products for {abs(budget - leaving_budget):.2f} leva.")