# •	На първия ред - капацитет на залата - цяло число в интервала [50... 150]
# На всеки следващ ред до команда "Movie time!":
# o	Брой хора влизащи в киното - цяло число в интервала [1… 15]
hall_capacity = int(input())
command = input()
money_sum = 0
while command != 'Movie time!':
    come_in_people = int(command)
    if hall_capacity < come_in_people:
        print("The cinema is full.")
        break
    if come_in_people % 3 == 0:
        money_sum += (come_in_people * 5) - 5
    else:
        money_sum += come_in_people * 5
    hall_capacity -= come_in_people
    command = input()
if command == 'Movie time!':
    print(f"There are {hall_capacity} seats left in the cinema.")
print(f"Cinema income - {money_sum} lv.")

