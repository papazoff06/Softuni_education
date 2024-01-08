import re
total_income = 0
some_list =[]

pattern = r"%([A-Z][a-z]+)%\.*[^\$\%\|\.]*<([A-Z]?[a-z]*)>\.*[^\$\%\|\.]*\|(\d+)\|[A-Za-z\.]*(\d+\.?\d?)\$"

command = input()
while command != 'end of shift':
    match = re.search(pattern, command)
    if match:
        customer, product, count, price = match.groups()
        current_price = int(count) * float(price)
        total_income += current_price
        print(f"{customer}: {product} - {current_price:.2f}")
    command = input()
print(f"Total income: {total_income:.2f}")