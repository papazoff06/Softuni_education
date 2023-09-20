m2 = float(input())
m2_price = float(m2 * 7.61)
price_with_discount = m2_price * 0.82
discount = float(m2_price - price_with_discount)
print(f'The finl price is: {price_with_discount:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')

