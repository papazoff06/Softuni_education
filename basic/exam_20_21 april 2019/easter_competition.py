easter_bred_count  = int(input())
score_count = 0
best_beaker = ''
best_score = 0
for bred in range(easter_bred_count):
    current_score = 0
    beaker_name = input()
    command = input()
    while command != 'Stop':
        score = int(command)
        current_score += score
        command = input()
    if current_score > best_score:
        best_score = current_score
        best_beaker = beaker_name
    print(f"{beaker_name} has {current_score} points.")
    if best_beaker == beaker_name:
        print(f"{best_beaker} is the new number 1!")
print(f"{best_beaker} won competition with {best_score} points!")





