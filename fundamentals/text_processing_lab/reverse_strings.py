# command = input()
#
# while True:
#     if command == "end":
#         break
#     else:
#         current_str = command
#         print(f"{current_str} = {current_str[::-1]}")
#     command = input()
#
# or

command = input()
while command != 'end':
    current_comand = command
    print(f"{current_comand} = {current_comand[::-1]}")
    command = input()