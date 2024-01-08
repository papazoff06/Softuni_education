number_of_heroes = int(input())
max_HP = 100
max_MP = 200
heroes_dict = {}
for heroes in range(number_of_heroes):
    command = input().split(' ')
    hero_name = command[0]
    HP = int(command[1])
    MP = int(command[2])
    heroes_dict[hero_name] = {'HP': HP, 'MP': MP}

command = input()
while command != "End":
    current_command = command.split(' - ')
    if current_command[0] == "CastSpell":
        hero_name = current_command[1]
        MP_needed = int(current_command[2])
        spell_name = current_command[3]
        if heroes_dict[hero_name]['MP'] >= MP_needed:
            heroes_dict[hero_name]['MP'] = heroes_dict[hero_name]['MP'] - MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif current_command[0] == 'TakeDamage':
        hero_name = current_command[1]
        damage = int(current_command[2])
        attacker = current_command[3]
        heroes_dict[hero_name]['HP'] = heroes_dict[hero_name]['HP'] - damage
        if heroes_dict[hero_name]['HP'] > 0:
            print(
                f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
        else:
            del heroes_dict[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')
    elif current_command[0] == "Recharge":
        hero_name = current_command[1]
        amount = int(current_command[2])
        if heroes_dict[hero_name]['MP'] + amount > max_MP:
            print(f"{hero_name} recharged for {max_MP - heroes_dict[hero_name]['MP']} MP!")
            heroes_dict[hero_name]['MP'] = max_MP
        else:
            print(f"{hero_name} recharged for {amount} MP!")
            heroes_dict[hero_name]['MP'] = heroes_dict[hero_name]['MP'] + amount
    elif current_command[0] == "Heal":
        hero_name = current_command[1]
        amount = int(current_command[2])
        if heroes_dict[hero_name]['HP'] + amount >= max_HP:
            print(f"{hero_name} healed for {max_HP - heroes_dict[hero_name]['HP']} HP!")
            heroes_dict[hero_name]['HP'] = max_HP
        else:
            print(f"{hero_name} healed for {amount} HP!")
            heroes_dict[hero_name]['HP'] = heroes_dict[hero_name]['HP'] + amount

    command = input()

for key, values in heroes_dict.items():
    print(f'{key}')
    for result, result_2 in values.items():
        print(f'  {result}: {result_2}')
