first_char = input()
second_char = input()
text = input()
result = 0

for char in range(ord(first_char), ord(second_char)):
    for symbol in text:
        if chr(char) == symbol:
            result += ord(symbol)
print(result)


