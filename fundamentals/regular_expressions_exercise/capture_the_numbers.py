import re

pattern = r"\d+"

text = input()
while text:
    matched = re.findall(pattern, text)
    for i in matched:
        print(i, end=' ')
    text = input()

