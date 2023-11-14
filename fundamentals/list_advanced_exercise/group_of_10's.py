numbers = [int(number) for number in input().split(', ')]
current_group = 10
while numbers:
    filtered_numbers = [i for i in numbers if i <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers}")
    current_group += 10
    numbers = [i for i in numbers if i not in filtered_numbers]
