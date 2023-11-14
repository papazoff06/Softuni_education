input_string = input().split(' ')
command = input()
while command != '3:1':
    commands = command.split(' ')
    if commands[0] == 'merge':
        start = int(commands[1])
        end = int(commands[2])
        if start < 0:
            start = 0
        if end > len(input_string) - 1:
            end = len(input_string) - 1
        merged = [''.join(input_string[start:end + 1])]
        input_string[start:end + 1] = merged
    elif commands[0] == 'divide':
        index = int(commands[1])
        partitions = int(commands[2])
        element = input_string[index]
        separate_element = []
        partition_length = len(element) // partitions
        for current_element_index in range(partitions):
            if current_element_index != partitions - 1:
                separate_element.append(element[current_element_index
                                                * partition_length: (current_element_index + 1)  * partition_length])
            else:
                separate_element.append(element[current_element_index * partition_length:])
        input_string[index:index + 1] = separate_element
    command = input()
print(' '.join(input_string))












#     command = input()
# print(*input_string)

    #     my_list.append(merge)
    # elif commands[0] == 'divide':
    #     index = commands[1]
    #     partition = commands[2]
    #     divide = [input_string[int(index)].split(partition)]



# #     print(commands)
#     command = input()
# print(my_list)
