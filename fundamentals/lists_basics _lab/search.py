n= int(input())
word = input()

my_list = []
for i in range(n):
    some_string = input()
    my_list.append(some_string)
print(my_list)
for j in range(len(my_list) - 1, - 1, - 1):
    element = my_list[j]
    if word not in element:
        my_list.remove(element)
print(my_list)