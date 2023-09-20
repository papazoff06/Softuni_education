# От конзолата се четaт два реда:
# •	Брой дни – цяло число в интервала [1 … 5]
# •	Брой часове за всеки един от дните - цяло число в интервала [1 … 24]
days_count = int(input())
hours_count = int(input())
price = 0
total_price = 0

for days in range(1, days_count + 1):
    if days % 2 == 0:
        for hours in range(1, hours_count + 1):
            if not hours % 2 == 0:
                price += 2.50
            else:
                price += 1
    elif not days % 2 == 0:
        for hours in range(1, hours_count + 1):
            if hours % 2 == 0:
                price += 1.25
            else:
                price += 1
    print(f"Day: {days} - {price:.2f} leva")
    total_price += price
    price = 0
print(f"Total: {total_price:.2f} leva")




