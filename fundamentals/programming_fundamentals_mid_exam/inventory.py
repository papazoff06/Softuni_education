journal = input().split(', ')
command = input()

while command != 'Craft!':
    current_command = command.split(' - ')
    if current_command[0] == 'Collect':
        item = current_command[1]
        if item in journal:
            continue
        else:
            journal.append(item)
    elif current_command[0] == 'Drop':
        item = current_command[1]
        if item in journal:
            journal.remove(item)
    elif current_command[0] == 'Combine Items':
        new_word = current_command[1].split(':')
        old_item = new_word[0]
        new_item = new_word[1]
        idx = journal.index(old_item)
        if old_item in journal:
            journal.insert(idx + 1, new_item)
    elif current_command[0] == 'Renew':
        item = current_command[1]
        if item in journal:
            idx = journal.index(item)
            journal.pop(idx)
            journal.append(item)
    command = input()
print(', '.join(journal))