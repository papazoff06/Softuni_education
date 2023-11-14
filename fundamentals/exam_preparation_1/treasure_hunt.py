initial_treasure_chest = input().split('|')
stolen_item = []
stolen_treasure_sum = 0
command = input()
while command != 'Yohoho!':
    current_command = command.split()
    if current_command[0] == 'Loot':
        for word in current_command[1: len(current_command)]:
            if word in initial_treasure_chest:
                continue
            else:
                initial_treasure_chest.insert(0, word)
    elif current_command[0] == 'Drop':
        index = int(current_command[1])
        if 0 < abs(index) < len(initial_treasure_chest):
            x = initial_treasure_chest.pop(index)
            initial_treasure_chest.append(x)
        else:
            continue
    elif current_command[0] == 'Steal':
        count = int(current_command[1])
        if count > len(initial_treasure_chest):
            removed = initial_treasure_chest
            print(', '.join(removed))
        else:
            removed = initial_treasure_chest[-count:]
            del initial_treasure_chest[-count:]
            print(', '.join(removed))

    command = input()
for i in initial_treasure_chest:
    stolen_treasure_sum += len(i)


if len(initial_treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    average = stolen_treasure_sum / len(initial_treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
