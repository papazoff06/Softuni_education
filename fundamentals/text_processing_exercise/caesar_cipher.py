text = input()

result = ''
for word in text:
    result += chr(ord(word) + 3)
print(result)
