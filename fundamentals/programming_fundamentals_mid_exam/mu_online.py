count_of_rooms = input().split('|')
max_health = 100
current_health = max_health
bitcoins = 0
room_counter = 0
for i in count_of_rooms:

    command = i.split(' ')
    current_command, number = command[0], int(command[1])
    if current_command == 'potion':
        room_counter += 1
        if current_health + number > max_health:
            difference = max_health - current_health
            current_health += difference
            print(f"You healed for {difference} hp.")
            print(f"Current health: {current_health} hp.")
        else:
            current_health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {current_health} hp.")
    elif current_command == 'chest':
        room_counter += 1
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        room_counter += 1
        current_health -= number
        if current_health > 0:
            print(f"You slayed {current_command}.")
        else:
            print(f"You died! Killed by {current_command}." )
            print(f"Best room: {room_counter}")
            exit()

if room_counter == len(count_of_rooms):
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f"Health: {current_health}")





