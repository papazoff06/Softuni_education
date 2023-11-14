pair_of_rows = int(input())
average = 4.50
some_dict = {}


for next_pair in range(pair_of_rows):
    students_name  = input()
    grade = float(input())
    if students_name not in some_dict.keys():
        some_dict[students_name] = grade

    else:
        some_dict[students_name] += grade
        some_dict[students_name] /= 2

for key, value in some_dict.items():
    if value >= average:
        print(f"{key} -> {value:.2f}")


