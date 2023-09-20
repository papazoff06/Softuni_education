count_of_games = int(input())
Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

for games in range(count_of_games):
    current_game = input()
    if current_game == 'Hearthstone':
        Hearthstone += 1
    elif current_game == 'Fornite':
        Fornite += 1
    elif current_game =='Overwatch':
        Overwatch += 1
    else:
        Others += 1
percentage_Hearthstone = (Hearthstone / count_of_games) * 100
percentage_Fornite = (Fornite / count_of_games) * 100
percentage_Overwatch = (Overwatch / count_of_games) * 100
percentage_Others = (Others / count_of_games) * 100

print(f"Hearthstone - {percentage_Hearthstone:.2f}%")
print(f"Fornite - {percentage_Fornite:.2f}%")
print(f"Overwatch - {percentage_Overwatch:.2f}%")
print(f"Others - {percentage_Others:.2f}%")