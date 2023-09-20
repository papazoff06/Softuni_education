# # 2⋅π⋅r
# S=π.r2

from math import pi

r = float(input())

calculated_area = 2 * pi * r
calculated_parameter = pi * r ** 2
print(f'{calculated_parameter:.2f}')
print(f'{calculated_area:.2f}')


