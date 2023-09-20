import math
wall_high = int(input())
wall_width = int(input())
percentage_not_for_paint = int(input())


hall_squares_for_paint = math.ceil((wall_width * wall_high * 4) * (100 - percentage_not_for_paint) / 100)
liters_paint_sum = 0
command = input()
while command != "Tired!":
    liters_paint = int(command)
    liters_paint_sum += liters_paint
    if liters_paint_sum >= hall_squares_for_paint:
        break
    command = input()
if liters_paint_sum > hall_squares_for_paint:
    print(f"All walls are painted and you have {liters_paint_sum - hall_squares_for_paint} l paint left!")
elif hall_squares_for_paint == liters_paint_sum:
    print("All walls are painted! Great job, Pesho!")
if command == "Tired!":
    print(f"{hall_squares_for_paint - liters_paint_sum} quadratic m left.")





