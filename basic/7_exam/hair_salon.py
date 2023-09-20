target_for_day = int(input())
command = input()
total_sum = 0


while command != 'closed':
    service = command
    if service == 'haircut':
        service_nime = input()
        if service_nime == 'mens':
            total_sum += 15
        elif service_nime == 'ladies':
            total_sum += 20
        elif service_nime == 'kids':
            total_sum += 10
    elif service == 'color':
        service_nime = input()
        if service_nime == 'touch up':
            total_sum += 20
        elif service_nime == 'full color':
            total_sum = 30


    if total_sum >= target_for_day:
        break
    command = input()

if total_sum < target_for_day:
    print(f"Target not reached! You need {target_for_day - total_sum}lv. more.")
    print(f"Earned money: {total_sum}lv.")
else:
    print("You have reached your target for the day!")
    print(f"Earned money: {total_sum}lv.")
