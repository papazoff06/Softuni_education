# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.
CHICEN_MENU = 10.35
FISH_MENU = 12.40
VEGAN_MENU = 8.15
DESSERT = (CHICEN_MENU + FISH_MENU + VEGAN_MENU) * 0.20
DELIVERY = 2.50

count_chicen_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

order_price = ((CHICEN_MENU * count_chicen_menu) + (FISH_MENU * count_fish_menu) + (VEGAN_MENU * count_vegan_menu) + \
((CHICEN_MENU * count_chicen_menu) + (FISH_MENU * count_fish_menu) + (VEGAN_MENU * count_vegan_menu)) * 0.20 + DELIVERY)
print(round(order_price, 2))
