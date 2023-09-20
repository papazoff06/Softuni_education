# От конзолата първо се четат два реда:
# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"
tournament_count = int(input())
starting_score = int(input())
score_sum = 0
total_score = 0
wins = 0
import math
for _ in range(tournament_count):

    command = input()
    if command == 'W':
        score_sum += 2000
        wins += 1
    elif command == "F":
        score_sum += 1200
    elif command == 'SF':
        score_sum += 720
total_score = starting_score + score_sum
average_score = math.floor(score_sum / tournament_count)
percent_wins_tournament = wins / tournament_count * 100

print(f"Final points: {total_score}")
print(f"Average points: {average_score}")
print(f"{percent_wins_tournament:.2f}%")





