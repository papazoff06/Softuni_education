gift = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    if 'OutOfStock' in command:
        for i in range(len(gift)):
            if command[1] in gift[i]:
                gift[i] = 'None'
    elif 'Required' in command:
        for i in range(len(gift)):
            if i == int(command[2]):
                gift[i] = command[1]
    elif 'JustInCase' in command:
        gift[- 1] = command[1]
    command = input()
while 'None' in gift:
    gift.remove('None')
for i in gift:
    print(i, end=' ')
