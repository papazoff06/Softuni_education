import math
sugar = 0.950
flour = 0.750
# Вход
# От конзолата се чете 1 ред:
# •	 Броят на козунаците – цяло число в интервала [1 ... 100]
# За всеки козунак се чете:
# o	Количество изразходвана захар (грамове) – цяло число в интервала [1 … 10000]
# o	Количество изразходвано брашно (грамове) – цяло число в интервала [1 … 10000]
count_of_easter_bred = int(input())
whole_sugar = 0
whole_flour = 0
biggest_sugar = 0
biggest_flour = 0

for bred in range(count_of_easter_bred):
    spend_sugar = int(input())
    spend_flour = int(input())
    if spend_sugar > biggest_sugar:
        biggest_sugar = spend_sugar
    if spend_flour > biggest_flour:
        biggest_flour = spend_flour
    whole_sugar += spend_sugar
    whole_flour += spend_flour
needed_package_sugar = math.ceil(whole_sugar / 950)
needed_package_flour = math.ceil(whole_flour / 750)
print(f"Sugar: {needed_package_sugar}")
print(f"Flour: {needed_package_flour}")
print(f"Max used flour is {biggest_flour} grams, max used sugar is {biggest_sugar} grams.")


