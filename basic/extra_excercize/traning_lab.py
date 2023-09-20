w = float(input())
h = float(input())
w_in_meters = w * 100
h_in_meters = h * 100

corridor = 100
working_place_w = 120
working_place_h = 70
working_place = 1
entry_door = working_place
catedra = working_place * 2

count_working_place_in_w = w_in_meters  // working_place_w
count_working_place_in_h = ((h_in_meters - corridor) // working_place_h)
all_working_places = (count_working_place_in_w * count_working_place_in_h) - entry_door - catedra
print(all_working_places)

