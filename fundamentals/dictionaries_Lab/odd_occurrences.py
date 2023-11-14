elements = input().split()
elements = [x.lower() for x in elements]
odd = {}
for i in elements:
    if i not in odd:
        odd[i] = 0
    odd[i] += 1
for key, value in odd.items():
    if value % 2 != 0:
        print(key, end=' ')