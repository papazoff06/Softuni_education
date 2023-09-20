red_ball_count = 0
orange_ball_count = 0
yellow_ball_count = 0
white_ball_count = 0
black_ball_count = 0
other_colors_picked = 0
divides_from_black_balls = 0
score = 0

balls_count = int(input())

for i in range(balls_count):
    ball = input()
    if ball == 'red':
        score += 5
        red_ball_count += 1
    elif ball == 'orange':
        score += 10
        orange_ball_count += 1
    elif ball == 'yellow':
        score += 15
        yellow_ball_count += 1
    elif ball == 'white':
        score += 20
        white_ball_count += 1
    elif ball == 'black':
        score //= 2
        divides_from_black_balls += 1
    else:
        other_colors_picked += 1
        continue
print(f"Total points: {score}")
print(f"Red balls: {red_ball_count}")
print(f"Orange balls: {orange_ball_count}")
print(f"Yellow balls: {yellow_ball_count}")
print(f"White balls: {white_ball_count}")
print(f'Other colors picked: {other_colors_picked}')
print(f'Divides from black balls: {divides_from_black_balls}')
