days_count = int(input())

liters_count = 0
degrees_sum = 0

for i in range(days_count):
    rakia_quantity = float(input())
    degrees = float(input())

    liters_count += rakia_quantity
    whole_degrees = rakia_quantity * degrees
    degrees_sum += whole_degrees

average_degrees = degrees_sum / liters_count
print(f'{liters_count:.2f}')
print(f'{average_degrees:.2f}')
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
elif 42 < average_degrees:
    print("Dilution with distilled water!")




