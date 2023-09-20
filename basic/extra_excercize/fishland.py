# •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
MUSSELS = 7.50
mackerel_price_in_kg = float(input())
sprinkle_price_in_kg = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())
# •	Паламуд – 60% по-скъп от скумрията
# •	Сафрид – 80% по-скъп от цацата
bonito_price = mackerel_price_in_kg * 1.6
safrid_price = sprinkle_price_in_kg * 1.8

georgi_shopping_price = (bonito_kg * bonito_price) + (safrid_kg * safrid_price) + (mussels_kg * 7.50)
print(f'{georgi_shopping_price:.2f}')


