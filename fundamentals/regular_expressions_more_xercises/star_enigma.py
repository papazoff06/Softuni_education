import re
message_number = int(input())
message = ''
list_of_messages = []
pattern = r"[star]"
for i in range(message_number):
    current_message = input()
    match = re.findall(pattern, current_message, re.I)
    for letter in current_message:
        decrypt_letter = ord(letter) - len(match)
        message += chr(decrypt_letter)
    list_of_messages.append(message)
    message = ''
atacted_planets = []
destroed_planets = []

pattern_2 = r"\D*@([A-Za-z]+)(\.*[^\@\-\!\>]*)\:(\d+)(\.*[^\@\-\!\>]*)\!(A|D)!(\.*[^\@\-\!\>]*)->(\d+)(\.*[^\@\-\!\>]*)"
for message in list_of_messages:
    matched = re.search(pattern_2, message)
    if matched:
        planet_name = matched.group(1)
        planet_population = matched.group(3)
        attack_type = matched.group(5)
        if attack_type == 'A':
            atacted_planets.append(planet_name)
        elif attack_type == 'D':
            destroed_planets.append(planet_name)
        soldier_count = matched.group(7)
atacted_planets.sort()
destroed_planets.sort()
print(f'Attacked planets: {len(atacted_planets)}')
for a_planet in atacted_planets:
    print(f'-> {a_planet}')
print(f'Destroyed planets: {len(destroed_planets)}')
for d_planet in destroed_planets:
    print(f'-> {d_planet}')





