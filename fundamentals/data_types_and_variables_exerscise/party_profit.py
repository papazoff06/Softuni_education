group_size = int(input())
days_trip = int(input())

coins_count = 0

for day in range(1, days_trip + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        coins_count -= 3 * group_size
    if day % 5 ==0:
        coins_count += 20 * group_size
        if day % 3 == 0:
            coins_count -= 2 * group_size
    coins_count += 50 - (group_size * 2)

coins_per_person = int(coins_count / group_size)
print(f"{group_size} companions received {coins_per_person} coins each.")



