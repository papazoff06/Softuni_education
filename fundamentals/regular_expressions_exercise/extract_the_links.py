import re

pattern = r"(www\.[A-Za-z0-9\-\.]+\.[a-z]+)"
lane = input()
while lane:
    matched = re.search(pattern, lane)
    if matched:
        mail = matched.group(1)
        print(mail)
    lane = input()
