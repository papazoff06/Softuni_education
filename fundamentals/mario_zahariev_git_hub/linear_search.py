def linear_search(my_list: list, target: int):
    index = -1
    for i in range(len(my_list)):
        if my_list[i] == target:
            index = i
            return index
        else:
            continue


some_list = [1, 2, 3, 4, 5, 6]
target_1 = 7

result = linear_search(some_list, target_1)

if result != - 1:
    print(f"The target element {target_1} is at index {result}.")
else:
    print(f"The target element {target_1} was not found in the list.")
