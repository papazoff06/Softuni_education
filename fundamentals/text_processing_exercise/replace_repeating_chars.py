sequence = input()
result = ''
for first_letter in sequence:
    result += first_letter
    break
for i in range(len(sequence)):
    letter = sequence[i]
    if result[-1] == letter:
        continue
    else:
        result += letter

print(result)