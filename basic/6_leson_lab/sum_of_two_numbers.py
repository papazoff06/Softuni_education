# •	Първи ред – начало на интервала – цяло число в интервала [1...999]
# •	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# •	Трети ред – магическото число – цяло число в интервала [1...10000]
start_number = int(input())
final_number = int(input())
magic_number = int(input())
combination_is_found = False
combination_counter = 0

for first_number in range(start_number, final_number + 1):
    for second_number in range(start_number, final_number + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
        print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")



