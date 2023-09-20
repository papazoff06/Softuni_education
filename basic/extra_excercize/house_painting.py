# 1.	x – височината на къщата – реално число в интервала [2...100]
# 2.	y – дължината на страничната стена – реално число в интервала [2...100]
# 3.	h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]
x_house_hight = float(input())
y_lenght_wall = float(input())
h_triangle_wall = float(input())

green_paint_liter = 3.4
red_paint_liter = 4.3
door = 1.2 * 2
window = 1.5 * 1.5
front_wall = (x_house_hight * x_house_hight) - door
back_wall = (x_house_hight * x_house_hight)
sides_walls = (x_house_hight * y_lenght_wall) * 2 - (window * 2)
roof_sides = (x_house_hight * y_lenght_wall) * 2
roof_front_and_back = (x_house_hight * h_triangle_wall) * 2 / 2

green_paint_need = (front_wall + back_wall + sides_walls) / green_paint_liter
red_paint_need = (roof_sides + roof_front_and_back) / red_paint_liter
print(f'{green_paint_need:.2f}')
print(f'{red_paint_need:.2f}')
