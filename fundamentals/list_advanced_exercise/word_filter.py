text = input().split()
for i in text:
    if len(i) % 2 == 0:
        print(i)

# both of decisions are ok!

text = input().split()
new_list = [word for word in text if len(word) % 2 == 0]
print('\n'.join(new_list))