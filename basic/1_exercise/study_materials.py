#	Пакет химикали - 5.80 лв.
#	Пакет маркери - 7.20 лв.
#	Препарат - 1.20 лв (за литър



#Вход
#От конзолата се четат 4 числа:
#•	Брой пакети химикали - цяло число в интервала [0...100]
#	Брой пакети маркери - цяло число в интервала [0...100]
#•	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#•	Процент намаление - цяло число в интервала [0...100]
#Изход
#Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.

packs_of_pencels = int(input())
packs_of_marcers = int(input())
liters_of_detergent = int(input())
percent_discount = int(input()) / 100
final_price = ((packs_of_pencels * 5.80 + packs_of_marcers * 7.20 + liters_of_detergent * 1.20) -
      (packs_of_pencels * 5.80 + packs_of_marcers * 7.20 + liters_of_detergent * 1.20) * percent_discount)
print(final_price)
