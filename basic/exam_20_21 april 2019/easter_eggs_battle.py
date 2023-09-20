# 1.	Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# 2.	Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
# След това до получаване на команда "End" се четe многократно един ред:
# 3.	Победител - текст - "one" или "two"
eggs_count_player_one = int(input())
eggs_count_player_two = int(input())
command = input()
sum_of_eggs_player_one = eggs_count_player_one
sum_of_eggs_player_two = eggs_count_player_two
while command != 'End':
    winner = command
    if winner == 'one':
        sum_of_eggs_player_two -= 1
    elif winner == 'two':
        sum_of_eggs_player_one -= 1
    if sum_of_eggs_player_one <= 0:
        print(f"Player one is out of eggs. Player two has {sum_of_eggs_player_two} eggs left.")
        break
    elif sum_of_eggs_player_two <= 0:
        print(f"Player two is out of eggs. Player one has {sum_of_eggs_player_one} eggs left.")
        break
    command = input()
if command == 'End':
    print(f"Player one has {sum_of_eggs_player_one} eggs left.")
    print(f"Player two has {sum_of_eggs_player_two} eggs left.")
