list_of_characters = input().split(', ')
my_dict = {char: ord(char) for char in list_of_characters}
print(my_dict)

#or the same dessission

list_of_characters = input().split(', ')
my_dict = {}
for i in list_of_characters:
    key = i
    value = ord(i)
    my_dict[key] = value
print(my_dict)