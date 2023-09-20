# От конзолата се чете 1 ред:
# •	 Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
# За всяко яйце се чете:
# o	Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"
# Изход

count_of_painted_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0
color = ''

for eggs in range(count_of_painted_eggs):
    color = input()
    if color == 'red':
        red_eggs += 1
    elif color == 'orange':
        orange_eggs += 1
    elif color == 'blue':
        blue_eggs += 1
    elif color == 'green':
        green_eggs += 1
if red_eggs > max_eggs:
    max_eggs = red_eggs
    color = 'red'
if orange_eggs > max_eggs:
    max_eggs = orange_eggs
    color = 'orange'
if blue_eggs > max_eggs:
    max_eggs = blue_eggs
    color = 'blue'
if green_eggs > max_eggs:
    max_eggs = green_eggs
    color = 'green'
print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {color}")

