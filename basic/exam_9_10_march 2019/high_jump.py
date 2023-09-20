# Входът е поредица от цели числа в интервала [100…300]:
# •	На първия ред се прочита желаната от Тихомир Иванов височина в сантиметри
# •	На всеки следващ ред до приключване на програмата се прочита височината от скока на Иванов
wanted_high = int(input())
training_high = wanted_high - 30
jump_count = 0
failed = False
count_of_failed = 0

while not failed:
    jump = int(input())
    jump_count += 1
    if jump <= training_high:
        count_of_failed += 1
        if count_of_failed == 3:
            failed = True
    else:
        if training_high >= wanted_high:
            break
        training_high += 5
        count_of_failed = 0

if not failed:
    print(f"Tihomir succeeded, he jumped over {training_high}cm after {jump_count} jumps.")
else:
    print(f"Tihomir failed at {training_high}cm after {jump_count} jumps.")



