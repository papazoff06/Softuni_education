import re
bought_furniture = []
whole_sum = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        whole_sum += float(price) * int(quantity)
    command = input()
print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {whole_sum:.2f}')