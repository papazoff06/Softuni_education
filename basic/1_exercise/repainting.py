NYLON_PRICE = 1.5
PAINT_PRICE = 14.5
THINNER_PRICE = 5.0
BAG_PRICE = 0.40

nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

extra_nylon = 2
extra_paint = paint * 0.10

all_expenses = ((nylon + extra_nylon) * NYLON_PRICE + \
                (paint + extra_paint) * PAINT_PRICE + \
                (paint_thinner * THINNER_PRICE) + BAG_PRICE)
labor_amount = all_expenses * 0.30 * hours
total_price = all_expenses + labor_amount
print(total_price)
















