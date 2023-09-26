number_of_lines = int(input())

balanced = True
position = ''

for _ in range(number_of_lines):
    current_string = input()
    if current_string == '(' and position == '':
        position = 'open'
    elif current_string == '(' and position != '':
        balanced = False
    if current_string == ')' and position == 'open':
        position = ''
    elif current_string == ')' and position != 'open':
        balanced = False
if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')