n = int(input())
my_list = []
filtered = []
for i in range(n):
    number = int(input())
    my_list.append(number)
command = input()
if command == 'even':
    for check in my_list:
        if check % 2 == 0:
            filtered.append(check)
elif command == 'odd':
    for check in my_list:
        if check % 2!= 0:
            filtered.append(check)
elif command == 'negative':
    for check in my_list:
        if check < 0:
            filtered.append(check)
elif command == 'positive':
    for check in my_list:
        if check >= 0:
            filtered.append(check)
print(filtered)
