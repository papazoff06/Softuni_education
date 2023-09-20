wanted_profit = float(input())
cocktail_price_sum = 0

while cocktail_price_sum < wanted_profit:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        diff = wanted_profit - cocktail_price_sum
        print(f"We need {diff:.2f} leva more.")
        break
    cocktail_count = int(input())
    cocktail_price = len(cocktail_name) * cocktail_count
    if cocktail_price % 2 != 0:
        cocktail_price *= 0.75
    cocktail_price_sum += cocktail_price
if cocktail_price_sum >= wanted_profit:
    print("Target acquired.")
print(f"Club income - {cocktail_price_sum:.2f} leva.")
