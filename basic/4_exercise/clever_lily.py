lily_age = int(input())
washer_machine = float(input())
doll_price = int(input())
total_money = 0
doll_count = 0

for birthday in range(1, lily_age + 1):
    if birthday % 2 == 0:
        total_money += birthday * 10 / 2
        total_money -= 1
    else:
        total_money += doll_price

if total_money >= washer_machine:
    diff = total_money - washer_machine
    print(f"Yes! {diff:.2f}" )
else:
    short = washer_machine - total_money
    print(f'No! {short:.2f}')




