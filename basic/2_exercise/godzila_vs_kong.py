budget = float(input())
extras = int(input())
clothes_price = float(input())
# Известно е, че:
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
decor = budget * 0.10
clothes = extras * clothes_price
if extras > 150:
    clothes *= 0.90
final_price = decor + clothes

if decor + clothes > budget:
    print('Not enough money!')
    print(f'Wingard needs {final_price - budget:.2f} leva more.')
elif decor + clothes <= budget:
    print('Action!')
    print(f'Wingard starts filming with {budget - final_price:.2f} leva left.')


