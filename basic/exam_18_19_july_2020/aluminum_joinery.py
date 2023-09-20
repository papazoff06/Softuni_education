joinery_count = int(input())
joinery_kind = input()
delivery_kind = input()

price = 0

if joinery_count < 10:
    print("Invalid order")
else:
    if joinery_kind == '90X130':
        price = 110
        if 30 < joinery_count <= 60:
            price *= 0.95
        elif joinery_count > 60:
            price *= 0.92
    elif joinery_kind == '100X150':
        price = 140
        if 40 < joinery_count <= 80:
            price *= 0.94
        elif joinery_count > 80:
            price *= 0.90
    elif joinery_kind == '130X180':
        price = 190
        if 20 < joinery_count <= 50:
            price *= 0.93
        elif joinery_count > 50:
            price *= 0.88
    elif joinery_kind == '200X300':
        price = 250
        if 25 < joinery_count <= 50:
            price *= 0.91
        elif joinery_count > 50:
            price *= 0.86
    final_price = price * joinery_count
    if delivery_kind == 'With delivery':
        final_price += 60
    elif delivery_kind =='Without delivery':
        final_price = final_price
    if joinery_count > 99:
        final_price *= 0.96
    print(f"{final_price:.2f} BGN")
