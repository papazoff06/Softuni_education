key = input().split()
index = 0
result = ''
command = input()

while command != 'find':
    current_string = command
    for i in current_string:
        decrypt = ord(i) - int(key[index])
        result += chr(decrypt)
        index += 1
        if index >= len(key):
            index = 0

    start_coordinates = result.index('<')
    end_coordinates = result.index('>')
    coordinates = result[start_coordinates + 1: end_coordinates]
    type = result.split('&')
    print(f"Found {type[1]} at {coordinates}")
    result = ''
    index = 0
    command = input()



