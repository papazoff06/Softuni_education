# 1.	Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry"
# 2.	Размерът на сета - текст с възможности: "small" или "big"
# 3.	Брой на поръчаните сетове - цяло число в интервала [1 … 10000]
# Изход
fruit = input()
set_size = input()
count_of_sets = int(input())
price_per_set = 0

if fruit == 'Watermelon':
    if set_size == 'small':
        price_per_set = 56 * 2
    elif set_size == 'big':
        price_per_set = 28.70 * 5
elif fruit == 'Mango':
    if set_size == 'small':
        price_per_set = 36.66 * 2
    elif set_size == 'big':
        price_per_set = 19.60 * 5
elif fruit == 'Pineapple':
    if set_size == 'small':
        price_per_set = 42.10 * 2
    elif set_size == 'big':
        price_per_set = 24.80 * 5
elif fruit == 'Raspberry':
    if set_size == 'small':
        price_per_set = 20 * 2
    elif set_size == 'big':
        price_per_set = 15.20 * 5
whole_price = count_of_sets * price_per_set
if 400 <= whole_price <=1000:
    whole_price *= 0.85
elif whole_price > 1000:
    whole_price /= 2
print(f"{whole_price:.2f} lv.")

