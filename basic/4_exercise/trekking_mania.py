mussala_group = 0
monbalan_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0

climbers_group_count = int(input())

for i in range(climbers_group_count):
    current_climbers = int(input())
    if current_climbers < 6:
        mussala_group += current_climbers
    elif current_climbers < 13:
        monbalan_group += current_climbers
    elif current_climbers < 26:
        kilimanjaro_group += current_climbers
    elif current_climbers < 41:
        k2_group += current_climbers
    elif 41 <= current_climbers:
        everest_group += current_climbers
total_climbers = mussala_group + monbalan_group + kilimanjaro_group + k2_group + everest_group

mussala_percent = mussala_group / total_climbers * 100
monbalan_percent = monbalan_group / total_climbers * 100
kilimanjaro_percent = kilimanjaro_group / total_climbers * 100
k2_percent = k2_group / total_climbers * 100
everest_percent = everest_group / total_climbers * 100

print(f'{mussala_percent:.2f}%')
print(f'{monbalan_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
