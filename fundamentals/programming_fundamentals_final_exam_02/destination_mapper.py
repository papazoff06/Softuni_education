import re
text = input()
travel_points = 0
some_list = []
pattern = r'(=|/)([A-Z][A-Za-z]{2,})\1'
matched = re.findall(pattern, text)
for match in matched:
    some_list.append(match[1])
    travel_points += len(match[1])
result = ', '.join(some_list)
print(f'Destinations: {result}')
print(f'Travel Points: {travel_points}')




