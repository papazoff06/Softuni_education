import re

text = input()
length_valid_emojis = [] 

pattern = r"(\:{2}|\*{2})([A-Z][a-z]{2,})(\1)"
matched = re.findall(pattern, text)

cool_threshold = 1
only_cool_emojis = []
emoji_cool = 0
trshold_str = ''
for i in text:
    trshold_str = ''
    if i.isdigit():
        trshold_str += i
for j in trshold_str:
    cool_threshold *= int(j)

for match in matched:
    temporary = ''
    temporary += match[0]
    temporary += match[1]
    temporary += match[2]
    length_valid_emojis.append(temporary)
    temporary = ''

print(f"Cool threshold: {cool_threshold}")
for emoji in length_valid_emojis:
    emoji_cool = 0
    search_word = emoji[2:-2]
    for letter in search_word:
        emoji_cool += ord(letter)
    if emoji_cool >= cool_threshold:
        only_cool_emojis.append(emoji)
        emoji_cool = 0

print(f"{len(length_valid_emojis)} emojis found in the text. The cool ones are:")
for cool_emoji in only_cool_emojis:
    print(cool_emoji)