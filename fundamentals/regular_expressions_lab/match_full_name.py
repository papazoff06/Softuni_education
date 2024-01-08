import re
names = input()

pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'

mach = re.findall(pattern, names)
for name in mach:
    print(name, end=' ')