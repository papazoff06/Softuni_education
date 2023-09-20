command = input()
sum_prime = 0
sum_non_prime = 0
while command != 'stop':
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for num in range(2, current_number):
        if current_number % num == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += current_number
    else:
        sum_non_prime += current_number

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
