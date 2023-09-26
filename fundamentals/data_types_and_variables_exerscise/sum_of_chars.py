number_of_letters = int(input())
sum_of_characters = 0
for character in range(number_of_letters):
    current_letter = input()
    sum_of_characters += ord(current_letter)
print(f'The sum equals: {sum_of_characters}')