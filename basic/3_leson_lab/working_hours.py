hour = int(input())
day_of_week = input()

if day_of_week == 'Monday' and 10 <= hour <= 18 \
        or day_of_week == 'Tuesday' and 10 <= hour <= 18 \
        or day_of_week == 'Wednesday' and 10 <= hour <= 18 \
        or day_of_week == 'Thursday' and 10 <= hour <= 18 \
        or day_of_week == 'Friday' and 10 <= hour <= 18 \
        or day_of_week == 'Saturday' and 10 <= hour <= 18:
    print('open')
else:
    print('closed')

