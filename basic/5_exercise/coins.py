change_money = float(input())

pennies = int(change_money * 100)

coin_count = 0

while pennies > 0:
    if pennies >= 200:
        pennies -= 200
    elif pennies >= 100:
        pennies -= 100
    elif pennies >= 50:
        pennies -= 50
    elif pennies >= 20:
        pennies -= 20
    elif pennies >= 10:
        pennies -= 10
    elif pennies >=5:
        pennies -= 5
    elif pennies >= 2:
        pennies -= 2
    elif pennies >= 1:
        pennies -= 1

    coin_count += 1
print(coin_count)
