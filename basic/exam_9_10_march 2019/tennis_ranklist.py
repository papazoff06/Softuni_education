# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"
import math
count_of_tournament = int(input())
start_score = int(input())
tournament_score_sum = 0
wins = 0
for i in range(count_of_tournament):
    current_tournament_stage = input()
    if current_tournament_stage == 'W':
        tournament_score_sum += 2000
        wins += 1
    elif current_tournament_stage == 'F':
        tournament_score_sum += 1200
    elif current_tournament_stage == 'SF':
        tournament_score_sum += 720
total_score = tournament_score_sum + start_score
average_score = tournament_score_sum / count_of_tournament
percentage = wins / count_of_tournament * 100
print(f"Final points: {total_score}")
print(f"Average points: {math.floor(average_score)}")
print(f"{percentage:.2f}%")


