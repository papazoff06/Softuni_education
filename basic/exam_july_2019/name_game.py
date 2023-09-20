# import sys
#
# command = input()
#
# max_score = - sys.maxsize
# winner_name = ""
# current_word_1 = 0
#
# while command != "Stop":
#     name = command
#     for i in range(len(name)):
#         i += current_word_1
#     for simbol in command:
#         simbol = ord()
#
#
#     command = input()
#
# print(f'The winner is {name} with {max_score} points!')
import sys

name = input()

max_score = -sys.maxsize
winner_name = ""

while name != "Stop":
    current_score = 0

    for letter in name:
        number = int(input())
        if number == ord(letter):
            current_score += 10
        else:
            current_score += 2
        if current_score >= max_score:
            max_score = current_score
            winner_name = name
    name = input()

print(f'The winner is {winner_name} with {max_score} points!')