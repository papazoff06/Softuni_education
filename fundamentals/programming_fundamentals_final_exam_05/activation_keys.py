text = input()

command = input()
while command != 'Generate':
    current_command = command.split('>>>')
    if current_command[0] == 'Contains':
        substring = current_command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif current_command[0] == 'Flip':
        upper_or_lower = current_command[1]
        startIndex = int(current_command[2])
        endIndex = int(current_command[3])
        if upper_or_lower == 'Upper':
            text = text[:startIndex] + text[startIndex:endIndex].upper() + text[endIndex:]
            print(text)
        else:
            text = text[:startIndex] + text[startIndex:endIndex].lower() + text[endIndex:]
            print(text)
    elif current_command[0] == 'Slice':
        startIndex = int(current_command[1])
        endIndex = int(current_command[2])
        text = text.replace(text[startIndex:endIndex], '')
        print(text)
    command = input()
print(f"Your activation key is: {text}")
