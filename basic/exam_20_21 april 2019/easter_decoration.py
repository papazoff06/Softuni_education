# •	кошничка за яйца (basket) – 1.50 лв.
# •	великденски венец (wreath) – 3.80 лв.
# •	шоколадов заек (chocolate bunny) – 7 лв.
basket_for_eggs = 1.50
easter_wreath = 3.80
chocolate_bunny = 7

# От конзолата първоначално се чете един ред:
# •	Брои на клиентите в магазина – цяло число [1… 100]
# •	След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# o	Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")
whole_purchase_sum = 0
customers_count = int(input())
for custom in range(customers_count):
    purchase = input()
    purchase_count = 0
    purchase_sum = 0
    while purchase != 'Finish':
        if purchase == 'basket':
            purchase_sum += basket_for_eggs
            purchase_count += 1
        elif purchase == 'wreath':
            purchase_sum += easter_wreath
            purchase_count += 1
        elif purchase == 'chocolate bunny':
            purchase_sum += chocolate_bunny
            purchase_count += 1
        purchase = input()
    if purchase_count % 2 == 0:
        purchase_sum *= 0.80
    whole_purchase_sum += purchase_sum
    print(f"You purchased {purchase_count} items for {purchase_sum:.2f} leva.")
average = whole_purchase_sum / customers_count
print(f"Average bill per client is: {average:.2f} leva.")