
some_string = input()
sum_of_points = 0
for i in some_string:
    if i == "a":
        sum_of_points += 1
    elif i == "e":
        sum_of_points += 2
    elif i == "i":
        sum_of_points += 3
    elif i == "o":
        sum_of_points += 4
    elif i == "u":
        sum_of_points += 5
print(sum_of_points)
