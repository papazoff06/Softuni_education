command = input()
some_dict = {}
while command != 'Sail':
    current_command = command.split('||')
    cities = current_command[0]
    population = int(current_command[1])
    gold = int(current_command[2])
    if cities not in some_dict.keys():
        some_dict[cities] = [population, gold]
    else:
        some_dict[cities][0] += population
        some_dict[cities][1] += gold
    command = input()

text = input()
while text != 'End':
    current_command = text.split('=>')
    if current_command[0] == 'Plunder':
        town = current_command[1]
        people = int(current_command[2])
        gold = int(current_command[3])
        some_dict[town][0] -= people
        some_dict[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if some_dict[town][0] <= 0 or some_dict[town][1] <= 0:
            del some_dict[town]
            print(f"{town} has been wiped off the map!")
    elif current_command[0] == 'Prosper':
        town = current_command[1]
        gold = int(current_command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            break
        some_dict[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {some_dict[town][1]} gold.")
    text = input()
if len(some_dict) > 0:
    print(f"Ahoy, Captain! There are {len(some_dict)} wealthy settlements to go to:")
    for key, value in some_dict.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

