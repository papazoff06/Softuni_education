text = input()

for index in range(len(text)):
    if ':' in text[index]:
        print(f':{text[index + 1]}')
