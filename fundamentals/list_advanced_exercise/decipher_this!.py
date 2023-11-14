# message = input().split(' ')
# deciphered = []
#
# for word in message:
#     ascii_char = [char for char in word if char.isdigit()]
#     word_list = [char for char in word if char not in ascii_char]
#
#     first_letter = chr(int(''.join(ascii_char)))
#     word_list[0], word_list[-1] = word_list[-1], word_list[0]
#     new_word = first_letter + ''.join(word_list)
#     deciphered.append(new_word)
#
# print(' '.join(deciphered))
#

secret_message = input().split()
final_word = []

for word in secret_message:
    digit_string = [i for i in word if i.isdigit()]
    word_no_digit = [j for j in word if not j.isdigit()]

    first_letter = chr(int(''.join(digit_string)))
    word_no_digit[0], word_no_digit[-1] = word_no_digit[-1], word_no_digit[0]
    set_word = first_letter + ''.join(word_no_digit)
    final_word.append(set_word)
print(' '.join(final_word))














