numbers = input().split()

my_new_list = []
round_list = []
for i in numbers:
    my_new_list.append(float(i))
for i in my_new_list:
    round_list.append(round(i))
print(round_list)
