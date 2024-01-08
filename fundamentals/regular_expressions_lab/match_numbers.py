import re
pattern = r"(^|(?<=\s))-?([0][1-9][0-9]*)(\.\d+)?($|(?=\s))"
some_string = input()

matches = re.finditer(pattern, some_string)
for match in matches:
    print(match.group(), end=' ')
