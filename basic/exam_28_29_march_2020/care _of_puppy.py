# •	Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# •	На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето на всяко хранене -
# цяло число в интервала [10 …1000]
bought_dog_food = int(input())
bought_dog_food_in_grams = bought_dog_food * 1000
whole_eaten_dog_food = 0
command = input()
while command != 'Adopted':
    eaten_dog_food = int(command)
    whole_eaten_dog_food += eaten_dog_food
    command = input()
if whole_eaten_dog_food <= bought_dog_food_in_grams:
    print(f"Food is enough! Leftovers: {bought_dog_food_in_grams - whole_eaten_dog_food} grams." )
else:
    print(f"Food is not enough. You need {whole_eaten_dog_food - bought_dog_food_in_grams} grams more.")


