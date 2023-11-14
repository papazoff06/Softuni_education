command = input()
parts = 0
taxes = 0
while command != 'special' and command != 'regular':
    current_part_price = float(command)
    if current_part_price < 0:
        print("Invalid price!")
        command = input()
        continue
    command = input()
    parts += current_part_price
    taxes += current_part_price * 0.20
total_price = parts + taxes
if total_price == 0:
    print("Invalid order!")
    exit()
else:
    if command == 'special':
        total_price *= 0.90
print(f"Congratulations you've just bought a new computer!")
print(f"Price without taxes: {parts:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print("-----------")
print(f"Total price: {total_price:.2f}$")
