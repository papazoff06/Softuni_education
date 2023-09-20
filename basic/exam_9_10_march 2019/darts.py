# Първоначално се чете един ред:
# •	Името на играча - текст
# След това до получаване на команда "Retire" се четат многократно по два реда:
# 1.	Поле – текст ("Single", "Double" или "Triple")
# 2.	Точки – цяло число в интервала [0… 100]

player_name = input()
start_scores = 301
unsuccessful = 0
successful = 0

command = input()
while command != 'Retire':
    scores = int(input())
    current_score = 0
    if command == 'Single':
        current_score += scores
    elif command == 'Double':
        current_score += scores * 2
    elif command == 'Triple':
        current_score += scores * 3
    if current_score < start_scores:
        successful += 1
        start_scores -= current_score
    elif current_score > start_scores:
        unsuccessful += 1
        continue
    command = input()
    if start_scores == 0:
        print(f"{player_name} won the leg with {successful} shots.")
if command == 'Retire':
    print(f"{player_name} retired after {unsuccessful} unsuccessful shots.")
