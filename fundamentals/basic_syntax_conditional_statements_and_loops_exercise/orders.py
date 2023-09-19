number_of_orders = int(input())
price = 0
for i in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())
    if capsule_price < 0.01 \
            or capsule_price > 100 \
            or days < 1 \
            or days > 31 \
            or needed_capsules_per_day < 1 \
            or needed_capsules_per_day > 2000:
        continue
    current_price = capsule_price * days * needed_capsules_per_day
    price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")
print(f"Total: ${price:.2f}")

