text = input().split()
first = text[0]
second = text[1]
result = 0
if len(first) < len(second):
    for index in range(len(first)):
        multiplay = ord(first[index]) * ord(second[index])
        result += multiplay
    for remind in range(len(first), len(second)):
        result += ord(second[remind])
elif len(first) > len(second):
    for index in range(len(second)):
        multiplay = ord(second[index]) * ord(first[index])
        result += multiplay
    for remind in range(len(second), len(first)):
        result += ord(first[remind])
else:
    for index in range(len(first)):
        multiplay = ord(first[index]) * ord(second[index])
        result += multiplay
print(result)