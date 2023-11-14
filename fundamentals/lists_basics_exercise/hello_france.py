collection_of_items = input().split('|')
budget = float(input())
bought_items = []
total_sum = 0

for i in collection_of_items:
    symbol = i.split('->')
    staff = symbol[0]
    staff_price = float(symbol[1])
    bought = False
    if staff == 'Clothes':
        if staff_price <= 50.00:
            bought = True
    elif staff == 'Shoes':
        if staff_price <= 35.00:
            bought = True
    elif staff == 'Accessories':
        if staff_price <= 20.50:
            bought = True
    if budget < staff_price:
        continue
    if bought:
        budget -= staff_price
        bought_items.append(staff_price * 1.4)
        total_sum += staff_price
for new_price in bought_items:
    print(f'{new_price:.2f}',end=' ')
profit = sum(bought_items) - total_sum
new_budget = budget + sum(bought_items)
print()
print(f"Profit: {profit:.2f}")
if new_budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")



