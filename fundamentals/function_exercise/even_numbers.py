numbers = input().split()
even_number = []
for i in numbers:
    if int(i) % 2 == 0:
        even_number.append(int(i))
print(even_number)
