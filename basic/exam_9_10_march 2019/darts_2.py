player_name = input()
start_scores = 301
unsuccessful = 0
successful = 0

command = input()
while command != 'Retire':
    scores = int(input())
    if command == 'Single':
        if start_scores >= scores:
            start_scores -= scores
            successful += 1
        else:
            unsuccessful += 1
    elif command == 'Double':
        if start_scores >= scores * 2:
            start_scores -= scores * 2
            successful += 1
        else:
            unsuccessful += 1
    elif command == 'Triple':
        if start_scores >= scores * 3:
            start_scores -= scores * 3
            successful += 1
        else:
            unsuccessful += 1
    if start_scores == 0:
        print(f"{player_name} won the leg with {successful} shots.")
        break
    command = input()
if command == 'Retire':
    print(f"{player_name} retired after {unsuccessful} unsuccessful shots.")

