from math import floor, ceil

time_first_player = int(input())
time_second_player = int(input())
time_third_player = int(input())

total_time_players = time_first_player + time_second_player + time_third_player
# 3.	След като сте намерили сбора от секундите трябва да ги превърнете в минути и секунди
# (например, ако сборът е 85 секунди това са 1 минута и 25 секунди, защото 1 минута има 60 секунди).
# Създайте две нови променливи. В първата изчислете колко минути е сборът от секунди като разделите сбора на 60.
# Във втората променлива изчислете секундите с помощта на деление с остатък (%), за да вземете остатъка при деление с 60.
# Например имате общ сбор от 134 секунди (2 минути и 14 секунди) след целочисленото деление (//) на 60 ще получим 2, а след
# делението с остатък (%) ще получим оставащите секунди(14):
total_time_players_in_minutes = total_time_players // 60
total_time_players_in_seconds = total_time_players % 60

total_time_players_in_minutes = floor(total_time_players_in_minutes)

if total_time_players_in_seconds < 10:
    print(f'{total_time_players_in_minutes}:0{total_time_players_in_seconds}')
else:
    print(f'{total_time_players_in_minutes}:{total_time_players_in_seconds}')
