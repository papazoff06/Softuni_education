some_string = input().split()

for word in some_string:
    new_string = word * len(word)
    print(new_string, end='')