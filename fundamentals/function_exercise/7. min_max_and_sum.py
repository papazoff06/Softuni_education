numbers = input().split()
my_list = []
for i in numbers:
    my_list.append(int(i))
print(f"The minimum number is {min(my_list)}")
print(f"The maximum number is {max(my_list)}")
print(f"The sum number is: {sum(my_list)}")