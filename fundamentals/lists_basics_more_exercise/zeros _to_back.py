single_string = input().split(', ')
list_1 = []
list_2 = []
for number in single_string:
    if number != '0':
        list_1.append(int(number))
    else:
        list_2.append(int(number))
final_list = list_1 + list_2
print(final_list)
