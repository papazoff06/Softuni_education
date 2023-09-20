from math import pi
kind_of_figure = input()
area = 0

if kind_of_figure == 'square':
    side = float(input())
    area = side * side

elif kind_of_figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif kind_of_figure == 'circle':
    r = float(input())
    area = pi * r ** 2

elif kind_of_figure == 'triangle':
    side_lenght = float(input())
    side_hight = float(input())
    area = (side_lenght * side_hight) / 2

print(f'{area:.3f}')





