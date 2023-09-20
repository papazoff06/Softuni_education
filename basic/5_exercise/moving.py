
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.
free_space_width = int(input())
free_space_length = int(input())
free_space_high = int(input())

total_space = free_space_width * free_space_high * free_space_length
left_space = total_space

command = input()

while command != 'Done':
    current_box = int(command)
    left_space -= current_box
    if left_space <= 0:
        break
    command = input()
if command == "Done":
    print(f"{left_space} Cubic meters left.")
else:
    print(f"No more free space! You need {-left_space} Cubic meters more.")




