# От конзолата се четат поредица от турнири до получаване на командата "End of tournaments":
# •	Име на турнира – текст
# •	За всеки турнир n на брой мача – цяло число в интервала [1…15]
# •	За всеки мач се четат по два реда:
# o	Точки, вкарани от отбора на Деси – цяло число в интервала от [0…150]
# o	Точки, вкарани от противниковия отбор – цяло число в интервала от [0…150]
command = input()
wins = 0
wost = 0
whole_games = 0
while command != 'End of tournaments':
    count_of_games = int(input())
    games = 0
    for i in range(count_of_games):
        desis_score = int(input())
        others_score = int(input())
        games += 1
        if desis_score > others_score:
            wins += 1
            print(f"Game {games} of tournament {command}: win with {abs(desis_score - others_score)} points.")
        else:
            wost += 1
            print(f"Game {games} of tournament {command}: lost with {abs(desis_score - others_score)} points.")
    whole_games += games
    command = input()
percent_wins_games = wins / whole_games * 100
percent_wost_games = wost / whole_games * 100
if command == 'End of tournaments':
    print(f'{percent_wins_games:.2f}% matches win')
    print(f'{percent_wost_games:.2f}% matches lost')
