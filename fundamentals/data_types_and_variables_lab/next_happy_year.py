year = int(input())

while True:
    year += 1
    year_in_str = str(year)
    if len(year_in_str) == len(set(year_in_str)):
        break
print(year_in_str)