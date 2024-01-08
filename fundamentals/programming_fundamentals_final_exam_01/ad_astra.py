import re
text = input()
pattern = r"(#|\|)([A-Za-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
total_calories = 0

some_dict = []
matched = re.findall(pattern, text)


for i in matched:
    calories = int(i[5])
    total_calories += calories
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for match in matched:
    item = match[1]
    data = match[3]
    calories = match[5]
    print(f"Item: {item}, Best before: {data}, Nutrition: {calories}")

