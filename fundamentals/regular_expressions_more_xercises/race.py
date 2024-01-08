
list_of_participants = input().split(', ')

some_dict = {}


command = input()
while command != 'end of race':
    current_player = ''
    current_number = 0
    current_name = command
    for i in current_name:
        if i.isalpha():
            current_player += i
        elif i.isdigit():
            current_number += int(i)
        else:
            continue
    if current_player not in list_of_participants:
        command = input()
        continue
    else:
        if current_player not in some_dict:
            some_dict[current_player] = current_number
        else:
            some_dict[current_player] += int(current_number)
    command = input()
sorted_winners = sorted(some_dict.items(), key=lambda x: x[1], reverse=True)
final = dict(sorted_winners)
some_list = []
for i in final:
    some_list.append(i)
print(f"1st place: {some_list[0]}")
print(f"2nd place: {some_list[1]}")
print(f"3rd place: {some_list[2]}")



