# text = input()
# command = input()
# while command != 'Decode':
#     commands = command.split('|')
#     action = commands[0]
#     if action == 'Move':
#         number_of_letters = int(commands[1])
#         text = text[number_of_letters:]+text[0:number_of_letters]
#     elif action == 'Insert':
#         index = int(commands[1])
#         value = commands[2]
#         text = text[:index] + value + text[index:]
#
#     elif action == 'ChangeAll':
#         substring = commands[1]
#         replacement = commands[2]
#         while substring in text:
#             text = text.replace(substring, replacement)
#     command = input()
# print(f"The decrypted message is: {text}")
# below is decision with functions

text = input()
def move_text(text, number_of_letters):
    text = text[number_of_letters:]+text[0:number_of_letters]
    return text


def insert_text(text, index, value):
    text = text[:index] + value + text[index:]
    return text


def change_text(text, substring, replacement):
    text = text.replace(substring, replacement)
    return text



command = input()
while command != 'Decode':
    current_command = command.split('|')
    if current_command[0] == 'Move':
        number_of_letters = int(current_command[1])
        text = move_text(text, number_of_letters)
    elif current_command[0] == 'Insert':
        index = int(current_command[1])
        value = current_command[2]
        text = insert_text(text, index, value)
    elif current_command[0] == 'ChangeAll':
        substring = current_command[1]
        replacement = current_command[2]
        text = change_text(text, substring, replacement)
    command = input()
print(f"The decrypted message is: {text}")

































