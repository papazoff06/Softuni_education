single_string = input()
list_1 = list()

for index, char in enumerate(single_string):
    if char.isupper():
        list_1.append(index)
print(list_1)


