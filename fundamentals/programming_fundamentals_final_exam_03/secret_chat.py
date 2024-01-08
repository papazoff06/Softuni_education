text = input()

command = input()
while command != 'Reveal':
    current_command = command.split(':|:')
    if current_command[0] == "InsertSpace":
        index = int(current_command[1])
        text = text[:index] + ' ' + text[index:]
        print(text)
    elif current_command[0] == "Reverse":
        substring = current_command[1]
        if substring in text:
            text = text.replace(substring, '')
            reverce = substring[::-1]
            text = text[:len(text)] + reverce
            print(text)
        else:
            print("error")
    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        while substring in text:
            text = text.replace(substring, replacement)
            print(text)
    command = input()
print(f"You have a new text message: {text}")
