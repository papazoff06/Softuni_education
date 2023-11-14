number_of_electrons = int(input())
my_list = []
for i in range(1, number_of_electrons + 1):
    max_electrons = 2 * i ** 2
    if max_electrons <= number_of_electrons:
        my_list.append(max_electrons)
        number_of_electrons -= max_electrons
if number_of_electrons > 0:
    my_list.append(number_of_electrons)
print(my_list)
