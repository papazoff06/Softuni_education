# 1.	Цена на моминското парти - реално число в интервала [1.00 … 10000.00]
# 2.	Брой любовни послания - цяло число в интервала [0… 1000]
# 3.	Брой восъчни рози - цяло число в интервала [0 … 1000]
# 4.	Брой ключодържатели - цяло число в интервала [0 … 1000]
# 5.	Брой карикатури - цяло число в интервала [0 … 1000]
# 6.	Брой късмети изненада -
love_message_price = 0.60
rose_price = 7.20
key_holder_price = 3.60
caricature_price = 18.20
surprise_price = 22

maiden_party_price = float(input())
love_message_count = int(input())
roseses_count = int(input())
key_holder_count = int(input())
caricatures_count = int(input())
surprises_count = int(input())

profit = (love_message_count * love_message_price) \
         + (roseses_count * rose_price) \
         + (key_holder_count * key_holder_price) \
         + (caricatures_count * caricature_price) \
         + (surprises_count * surprise_price)
if love_message_count + roseses_count + key_holder_count + caricatures_count + surprises_count >= 25:
    profit *= 0.65

final_price = profit * 0.90
left_money = final_price - maiden_party_price

if final_price >= maiden_party_price:
    print(f'Yes! {left_money:.2f} lv left.')
elif final_price < maiden_party_price:
    print(f'Not enough money! {-left_money:.2f} lv needed.')