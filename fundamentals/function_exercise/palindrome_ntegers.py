numbers= input().split(', ')

for i in numbers:
    if (i) == i[::-1]:
        palindrome = True
    else:
        palindrome = False
    print(palindrome)