numbers = input().split()
count_numbers_to_remove = int(input())
list_int_numbers = []
for i in numbers:
    list_int_numbers.append(int(i))
for remove_smallest in range(count_numbers_to_remove):
    list_int_numbers.remove(min(list_int_numbers))

print(*list_int_numbers, sep=', ')



