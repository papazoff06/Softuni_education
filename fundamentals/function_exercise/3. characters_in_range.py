def return_string(a, b):
    my_list = []
    for i in range(ord(a) + 1, ord(b)):
        my_list.append(chr(i))
    return my_list


first_string = input()
second_string = input()
final_result = return_string(first_string, second_string)
print(' '.join(final_result))
