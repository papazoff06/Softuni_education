command = input()

some_dict_quantity = {}
some_dict_price = {}

while command != 'buy':
    product_name, product_price, product_quantity = command.split()
    name = product_name
    price = float(product_price)
    quantity = int(product_quantity)
    if name not in some_dict_price.keys():
        some_dict_price[name] = 0
        some_dict_quantity[name] = 0
    some_dict_quantity[name] += quantity
    some_dict_price[name] = price
    command = input()
for key, value in some_dict_quantity.items():
    price = value * some_dict_price[key]
    print(f"{key} -> {price:.2f}")


