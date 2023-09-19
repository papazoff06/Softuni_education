budget = float(input())
price_for_1_kg_flour = float(input())
eggs = 0
bred_count = 0
loaf_price = price_for_1_kg_flour + (price_for_1_kg_flour * 0.75) + ((price_for_1_kg_flour * 1.25) / 4)
while budget > loaf_price:
    bred_count += 1
    eggs += 3
    if bred_count % 3 == 0:
        eggs -= bred_count - 2
    budget -= loaf_price
print(f"You made {bred_count} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")



