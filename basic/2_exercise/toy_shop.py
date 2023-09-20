PUZZLE_PRICE = 2.60
SPEAKING_DOLL_PRICE = 3
TEDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRACK_PRICE = 2
# 1.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.	Брой пъзели - цяло число в интервала [0… 1000]
# 3.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.	Брой миньони - цяло число в интервала [0 … 1000]
# 6.	Брой камиончета - цяло число в интервала [0 … 1000]
trip_price = float(input())
count_puzzles = int(input())
count_speaking_dolls = int(input())
count_tedy_bears = int(input())
count_minions = int(input())
count_tracks = int(input())

whole_sum = (count_puzzles * PUZZLE_PRICE) + (count_speaking_dolls * SPEAKING_DOLL_PRICE) + \
            (count_tedy_bears * TEDY_BEAR_PRICE) + (count_minions * MINION_PRICE) + (count_tracks * TRACK_PRICE)

dolls_count = count_puzzles + count_speaking_dolls + count_tedy_bears + count_minions + count_tracks
if dolls_count >= 50:
    whole_sum = whole_sum - (whole_sum / 4)
rent = whole_sum * 0.10
profit = whole_sum - rent
if profit >= trip_price:
    print(f' Yes! {profit - trip_price:.2f} lv left.')
else:
    print(f' Not enough money! {trip_price - profit:.2f} lv needed.')




# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия


