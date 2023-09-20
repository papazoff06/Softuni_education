command = input()

best_player = ''
gools = 0
is_hat_trick = False
while command != "END":
    curent_player_name = command
    players_gools = int(input())
    if players_gools > gools:
        best_player = curent_player_name
        gools = players_gools
        if 3 <= players_gools:
            is_hat_trick = True
        if players_gools >= 10:
            break
    command = input()
print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {gools} goals and made a hat-trick !!!")
else:
    print(f"He has scored {gools} goals.")







