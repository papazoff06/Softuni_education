count_of_numbers = int(input())
p_1 = 0
p_2 = 0
p_3 = 0
for i in range(count_of_numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        p_1 += 1
    if current_number % 3 == 0:
        p_2 += 1
    if current_number % 4 == 0:
        p_3 += 1
percentage_P_1 = p_1 / count_of_numbers * 100
percentage_P_2 = p_2 / count_of_numbers * 100
percentage_P_3 = p_3 / count_of_numbers * 100
print(f'{percentage_P_1:.2f}%')
print(f'{percentage_P_2:.2f}%')
print(f'{percentage_P_3:.2f}%')

