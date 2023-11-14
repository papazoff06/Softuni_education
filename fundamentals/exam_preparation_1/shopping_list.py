groceries = input().split('!')

command = input()
while command != 'Go Shopping!':
    current_command = command.split(' ')
    if current_command[0] == 'Urgent':
        item = current_command[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif current_command[0] == 'Unnecessary':
        item_for_remove = current_command[1]
        if item_for_remove in groceries:
            groceries.remove(item_for_remove)
    elif current_command[0] == 'Correct':
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in groceries:
            idx = groceries.index(old_item)
            groceries.pop(idx)
            groceries.insert(idx, new_item)
    elif current_command[0] == 'Rearrange':
        item = current_command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    command = input()
print(', '.join(groceries))

