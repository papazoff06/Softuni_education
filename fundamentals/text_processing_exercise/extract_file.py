# sequence = input().split('\\')
# file, extension = sequence[-1].split('.')
#
# print(f"File name: {file}")
# print(f"File extension: {extension}")

# or
sequence = input().split('\\')
for i in sequence:
    if '.' in i:
        first, second = i.split('.')
        print(f"File name: {first}")
        print(f"File extension: {second}")