number_of_pieces = int(input())
some_dict = {}
for pieces in range(number_of_pieces):
    current_piece = input().split('|')
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    some_dict[piece] = {composer: key}

command = input()
while command != 'Stop':
    current_command = command.split('|')
    if current_command[0] == 'Add':
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]
        if piece not in some_dict.keys():
            some_dict[piece] = {composer: key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif current_command[0] == 'Remove':
        piece = current_command[1]
        if piece in some_dict.keys():
            del some_dict[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif current_command[0] == 'ChangeKey':
        piece = current_command[1]
        key = current_command[2]
        if piece in some_dict.keys():
            some_dict[piece] = {composer: key}
            print(f'Changed the key of {piece} to {key}!')
        else:
            print(f'"Invalid operation! {piece} does not exist in the collection."')
    command = input()

for key, value in some_dict.items():
    for nested_key, nested_value in value.items():
        print(f"{key} -> Composer: {nested_key}, Key: {nested_value}")
