# От конзолата се четат 3 реда:
# 1.	Срок на договор – текст – "one", или "two"
# 2.	Тип на договор – текст – "Small",  "Middle", "Large"или "ExtraLarge"
# 3.	Добавен мобилен интернет – текст – "yes" или "no"
# 4.	Брой месеци за плащане - цяло число в интервала [1 … 24]
contract_term= input()
contract_type = input()
add_net = input()
count_of_monts = int(input())
mount_price = 0


if contract_term == 'one':
    if contract_type == 'Small':
        mount_price = 9.98
    elif contract_type == 'Middle':
        mount_price = 18.99
    elif contract_type == 'Large':
        mount_price = 25.98
    elif contract_type == 'ExtraLarge':
        mount_price = 35.99
elif contract_term == 'two':
    if contract_type == 'Small':
        mount_price = 8.58
    elif contract_type == 'Middle':
        mount_price = 17.09
    elif contract_type == 'Large':
        mount_price = 23.59
    elif contract_type == 'ExtraLarge':
        mount_price = 31.79
if add_net == 'yes':
    if mount_price <= 10:
        mount_price += 5.50
    elif mount_price <= 30:
        mount_price += 4.35
    elif mount_price > 30:
        mount_price += 3.85
whole_price = mount_price * count_of_monts
if contract_term == 'two':
    whole_price *= 0.9625
print(f"{whole_price:.2f} lv.")
