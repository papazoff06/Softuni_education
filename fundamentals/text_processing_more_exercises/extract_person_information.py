number = int(input())
name = ''
age = ''
for _ in range(number):
    text = input()
    name_start_idx = text.index('@')
    name_final_idx = text.index('|')
    name = text[name_start_idx + 1: name_final_idx]
    age_start_idx = text.index('#')
    age_final_idx = text.index('*')
    age = text[age_start_idx + 1: age_final_idx]
    print(f'{name} is {age} years old.')


