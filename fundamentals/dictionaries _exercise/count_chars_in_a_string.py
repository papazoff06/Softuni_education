text = input().split(' ')
new_text = ''.join(text)

my_dict = {}
for letter in new_text:
    if letter in new_text:
        my_dict[letter] = []
    my_dict[letter] = new_text.count(letter)
for i in my_dict:
    print(f'{i} -> {my_dict[i]}')

