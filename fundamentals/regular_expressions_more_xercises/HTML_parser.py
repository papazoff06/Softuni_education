import re

text = input()
title = re.findall(r"<title>(.*)</title>", text)
content = re.findall(r"<body>(.*)<\body>", text)
print(title, content)

#the problem isn't finished !