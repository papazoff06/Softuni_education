flor_count = int(input())
room_count = int(input())
Leter = ''

for current_flor in range(flor_count, 0 , - 1):
    if current_flor == flor_count:
        letter = 'L'
    elif current_flor % 2 == 0:
        letter = 'O'
    elif current_flor % 2 != 0:
        letter = 'A'

    for current_room in range( room_count + 1):
        print(f'{letter}{current_flor}{current_room}', end=' ')
    print()



