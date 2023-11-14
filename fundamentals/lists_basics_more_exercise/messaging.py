numbers_as_string = input().split()
message = input()
message_to_print = []

for current_number in numbers_as_string[::-1]:
    list_to_sum = []
    for i in current_number:
        list_to_sum.append(int(i))
    index = sum(list_to_sum)
    if index > len(message):
        continue
    message_to_print.append(message[index])
print(message_to_print)


