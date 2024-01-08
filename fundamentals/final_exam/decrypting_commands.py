text = input()

command = input()
while command != 'Finish':
    current_command = command.split(' ')
    if current_command[0] == 'Replace':
        currentChar = current_command[1]
        newChar = current_command[2]
        while currentChar in text:
            text = text.replace(currentChar, newChar)
            print(text)
    elif current_command[0] == 'Cut':
        startIndex = int(current_command[1])
        endIndex = int(current_command[2])
        if (startIndex >= 0 and endIndex >= 0) and (startIndex < len(text) and endIndex < len(text)):
            text = text.replace(text[startIndex:endIndex + 1], '')
            print(text)
        else:
            print("Invalid indices!")

    elif current_command[0] == 'Make':
        if current_command[1] == 'Upper':
            text = text.upper()
            print(text)
        elif current_command[1] == 'Lower':
            text = text.lower()
            print(text)
    elif current_command[0] == 'Check':
        string = current_command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif current_command[0] == 'Sum':
        startIndex = int(current_command[1])
        endIndex = int(current_command[2])
        new_text = ''
        result = 0
        if (startIndex >= 0 and endIndex >= 0) and (startIndex < len(text) - 1 and endIndex < len(text)):
            new_text = text[startIndex:endIndex + 1]
            for i in new_text:
                result += int(ord(i))
            print(result)
        else:
            print("Invalid indices!")
    command = input()