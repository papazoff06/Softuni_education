number_of_plants = int(input())
some_dict = {}

for i in range(number_of_plants):
    command = input().split('<->')
    plant = command[0]
    rarity = int(command[1])
    if plant not in some_dict.keys():
        some_dict[plant] = {'rarity': rarity, 'rating': []}
    some_dict[plant] = {'rarity': rarity, 'rating': []}
command = input()
while command != 'Exhibition':
    current_command = command.split(': ')
    if current_command[0] == 'Rate':
        given_command = current_command[1].split(' - ')
        plant = given_command[0]
        rating = int(given_command[1])
        if plant in some_dict.keys():
            some_dict[plant]['rating'] += [rating]
        else:
            print('error')
    elif current_command[0] == 'Update':
        given_command = current_command[1].split(' - ')
        plant = given_command[0]
        new_rarity = int(given_command[1])
        if plant in some_dict.keys():
            some_dict[plant]['rarity'] = new_rarity
        else:
            print('error')
    elif current_command[0] == 'Reset':
        plant = current_command[1]
        if plant in some_dict:
            some_dict[plant]['rating'] = []
        else:
            print('error')

    command = input()
print("Plants for the exhibition:")
for key, value in some_dict.items():
    if len(value['rating']) > 0:
        average = sum(value['rating']) / len(value['rating'])
        print(f"- {key}; Rarity: {value['rarity']}; Rating: {average:.2f}")
    else:
        average = 0
        print(f"- {key}; Rarity: {value['rarity']}; Rating: {average:.2f}")



























