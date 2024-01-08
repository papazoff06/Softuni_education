import re
text = input()
matched_words = []
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matched = re.findall(pattern, text)

if len(matched) <= 0:
    print("No word pairs found!")
else:
    print(f"{len(matched)} word pairs found!")
for i in matched:
    first_match = i[1]
    second_match = i[2]
    if first_match == second_match[::-1]:
        matched_words.append(first_match)

if len(matched_words) > 0:
    print(f'The mirror words are:')
    result = []
    for words in matched_words:
        result.append(f'{words} <=> {words[::-1]}')
    print(', '.join(result))
else:
    print('No mirror words!')





