import re
some_string = input()
search_word = input()
pattern = f"\\b{search_word}\\b"
result = re.findall(pattern, some_string, re.I)
print(len(result))