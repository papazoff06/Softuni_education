days_of_tournament = int(input())
total_win_money = 0
total_days_wins_count = 0
total_days_lost_count = 0

for days in range(days_of_tournament):
    command = input()
    today_win_money = 0
    today_wins_count = 0
    today_lost_count = 0
    while command != 'Finish':
        sport = command
        result = input()
        if result == 'win':
            today_win_money += 20
            today_wins_count += 1
        else:
            today_lost_count += 1
        command = input()
    if today_wins_count > today_lost_count:
        today_win_money *= 1.1
        total_win_money += today_win_money
        total_days_wins_count += 1
    else:
        total_days_lost_count += 1
        total_win_money += today_win_money
if total_days_wins_count > total_days_lost_count:
    total_win_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_win_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_win_money:.2f}")


