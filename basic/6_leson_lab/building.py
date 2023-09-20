number_of_flores = int(input())
rooms = int(input())
letter = ''

for current_flor in range(number_of_flores, 0, - 1 ):
    if current_flor == number_of_flores:
        letter = 'L'
    elif current_flor % 2 == 0:
        letter = 'O'
    elif current_flor % 2 != 0:
        letter = 'A'
    for current_room in range(rooms):
        print(f'{letter}{current_flor}{current_room}', end=" ")
    print()
