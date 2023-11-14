some_str = input()
digit = ''
alpha = ''
other = ''
for symbol in some_str:
    if symbol.isdigit():
        digit += symbol
    elif symbol.isalpha():
        alpha += symbol
    else:
        other += symbol
print(digit)
print(alpha)
print(other)



