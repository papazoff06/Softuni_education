cake_length = int(input())
cake_wide = int(input())

command = input()
whole_cake_peaces = cake_wide * cake_length

taken_peaces_count = 0

while command != 'STOP':
    taken_peaces = int(command)
    taken_peaces_count += taken_peaces
    if taken_peaces_count >= whole_cake_peaces:
        print(f'No more cake left! You need {taken_peaces_count - whole_cake_peaces} pieces more.')
        break

    command = input()
if command == 'STOP':
    print(f"{whole_cake_peaces - taken_peaces_count} pieces are left." )





