hours = int(input())
minutes = int(input())
minutes_new = 0
hours_new = 0

minutes_new = minutes + 15

if minutes >= 45:
    hours_new = hours + 1
    minutes_new = abs(60 - minutes_new)
else:
    hours_new = hours

if hours_new > 23:
    hours_new = 0
if minutes_new < 10:
    print(f"{hours_new}:{minutes_new:02d}")
else:
    print(f"{hours_new}:{minutes_new}")
















