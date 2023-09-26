tank_capacity = 255
sum_liters_of_water = 0
number = int(input())
for i in range(number):
    liters_of_water = int(input())
    if liters_of_water > tank_capacity:
        print('Insufficient capacity!')
        continue
    tank_capacity -= liters_of_water
    sum_liters_of_water += liters_of_water
print(sum_liters_of_water)
