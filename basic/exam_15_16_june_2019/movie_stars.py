# От конзолата първо се чете един ред:
# •	Бюджет за актьори - реално число в интервала [1000.0... 2 100 000.0]
# След това се четат многократно по един или два реда до команда "ACTION" или до изчерпване на бюджета:
# •	Име на актьор - текст
# Ако името на актьора съдържа по-малко или равно на 15 брой символи:
# o	Възнаграждение - реално число в интервала [250.0… 1 000 000.0]
budget = float(input())
command = input()


while command != 'ACTION':
    actors_name = command
    if len(actors_name) <= 15:
        salary = float(input())
        budget -= salary
    elif len(actors_name) > 15:
        salary = 0.20 * budget
        budget-= salary
    if budget < 0:
        break
    command = input()
if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")


