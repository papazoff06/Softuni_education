club_name = input()
games_count = int(input())
scores_count = 0
played_games = 0
wins_count = 0
remi_count = 0
lost_count = 0
if games_count == 0:
    print(f"{club_name} hasn't played any games during this season.")
else:
    for i in range(games_count):
        current_score = input()
        played_games += 1
        if current_score == 'W':
            scores_count += 3
            wins_count += 1
        elif current_score == 'D':
            scores_count += 1
            remi_count += 1
        elif current_score == 'L':
             scores_count = scores_count
             lost_count += 1
    print(f"{club_name} has won {scores_count} points during this season.")
    print("Total stats:")
    print(f"## W: {wins_count}")
    print(f"## D: {remi_count}")
    print(f"## L: {lost_count}")
    print(f"Win rate: {(wins_count / games_count) * 100:.2f}%")

