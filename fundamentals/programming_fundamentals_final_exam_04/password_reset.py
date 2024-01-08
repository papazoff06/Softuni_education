text = input()

command = input()
while command != 'Done':
    current_command = command.split(' ')
    if current_command[0] == 'TakeOdd':
        text = text[1:len(text):2]
        print(text)
    elif current_command[0] == 'Cut':
        index = int(current_command[1])
        length = int(current_command[2])
        text = text[:index]+text[index+length:]
        print(text)
    elif current_command[0] == 'Substitute':
        substring = current_command[1]
        substitute = current_command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {text}")