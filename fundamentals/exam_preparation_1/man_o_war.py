pirate_ship_str = input().split('>')
war_ship_str = input().split('>')
max_health = int(input())
pirate_ship = [int(x) for x in pirate_ship_str]
war_ship = [int(x) for x in war_ship_str]
command = input()
sunk = False
while command != 'Retire':
    current_command = command.split(' ')
    if current_command[0] == 'Fire':
        index = int(current_command[1])
        damage = int(current_command[2])
        if index >= 0 and index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                sunk = True
                print("You won! The enemy ship has sunken.")
                break

    elif current_command[0] == 'Defend':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        war_ship_damage = int(current_command[3])
        if start_index >= 0 and start_index < len(pirate_ship) and end_index >= 0 and end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= war_ship_damage
                if pirate_ship[i] <= 0:
                    sunk = True
                    print("You lost! The pirate ship has sunken.")
                    break

    elif current_command[0] == 'Repair':
        idx = int(current_command[1])
        healt = int(current_command[2])
        if idx >= 0 and idx < len(pirate_ship):
            if pirate_ship[idx] + healt > max_health:
                pirate_ship[idx] += max_health - pirate_ship[idx]
            pirate_ship[idx] += healt
    elif current_command[0] == 'Status':
        counter = 0
        for i in pirate_ship:
            if i < max_health * 0.20:
                counter += 1
        print(f"{counter} sections need repair.")
    command = input()
pirate_ship_status = sum(pirate_ship)
war_ship_status = sum(war_ship)
if not sunk:
    print(f"Pirate ship status: {pirate_ship_status}")
    print(f"Warship status: {war_ship_status}")













