numbers = input().split(', ')
beggars = int(input())
my_int_list = []
for integer in numbers:
    my_int_list.append(int(integer))
beggar_sum = []
index = 0
while index < beggars:
    current_beggar_sum = 0
    for current_index in range(index, len(numbers), beggars):
        current_beggar_sum += my_int_list[current_index]
    beggar_sum.append(current_beggar_sum)
    index += 1
print(beggar_sum)

