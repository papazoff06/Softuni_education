import sys
highest_value = - sys.maxsize
best_weight = 0
best_time = 0
best_quality = 0
number_of_snowballs = int(input())
for i in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_needed_for_snowball = int(input())
    quality_of_the_snowball = int(input())
    value_of_the_snowball = int(weight_of_the_snowball / time_needed_for_snowball) ** quality_of_the_snowball
    if value_of_the_snowball > highest_value:
        highest_value = value_of_the_snowball
        best_weight = weight_of_the_snowball
        best_time = time_needed_for_snowball
        best_quality = (quality_of_the_snowball)
print(f"{best_weight} : {best_time} = {highest_value} ({best_quality})")