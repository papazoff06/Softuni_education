import re
number = int(input())
pattern = r'(\D+)\>(([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|(.[^\<\>]+))\<\1'

for _ in range(number):
    password = input()
    matched = re.match(pattern, password)
    if matched:
        result = ''
        result += matched.group(3)
        result += matched.group(4)
        result += matched.group(5)
        result += matched.group(6)
        print(f'Password: {result}')
        result = ''
    else:
        print("Try another password!")




