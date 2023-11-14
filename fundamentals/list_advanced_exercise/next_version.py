string_version = input().split('.')
new_list = [string_version[0]+string_version[1]+string_version[2]]
final_list = []
first_number = 0
second_number = 0
third_number = 0

for i in new_list:
    number = int(i)
    number += 1
    final_list.append(str(number))
for i in final_list:
    first_number = i[0]
    second_number = i[1]
    third_number = i[2]
print(f'{first_number}.{second_number}.{third_number}')



