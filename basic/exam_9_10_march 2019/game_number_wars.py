first_player_name = input()
second_player_name = input()
first_player_points = 0
second_player_points = 0
command = input()
while command != 'End of game':
    first_player_card = int(command)
    second_player_card = int(input())
    if first_player_card == second_player_card:
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            print("Number wars!")
            print(f"{first_player_name} is winner with {first_player_points} points")
            break
        else:
            print("Number wars!")
            print(f"{second_player_name} is winner with {second_player_points} points")
            break
    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card
    elif second_player_card > first_player_card:
         second_player_points += second_player_card - first_player_card
    command = input()
if command == 'End of game':
    print(f"{first_player_name} has {first_player_points} points")
    print(f"{second_player_name} has {second_player_points} points")