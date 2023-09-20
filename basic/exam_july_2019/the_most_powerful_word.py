import math
import sys


command = input()
powerful_word = ''
word_sum = 0
max_sum = - sys.maxsize

while command != 'End of words':
    for letter in command:
        word_sum += ord(letter)
    if command[0] == 'a' or command[0] == 'e' or command[0] == 'i' \
            or command[0] == 'o' or command[0] == 'u' \
            or command[0] == 'y' or command[0] == 'A' \
            or command[0] == 'E' or command[0] == 'I' \
            or command[0] == 'O' or command[0] == 'U' \
            or command[0] == 'Y':
        word_sum *= len(command)
    else:
        word_sum /= len(command)
        word_sum = math.floor(word_sum)
    if word_sum > max_sum:
        max_sum = word_sum
        powerful_word = command
    command = input()
    word_sum = 0
print(f"The most powerful word is {powerful_word} - {max_sum}")






