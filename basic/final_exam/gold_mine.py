locations_per_day = int(input())


for _ in range(locations_per_day):
    expected_gold = float(input())
    digging_days_for_location = int(input())
    total_mined_gold = 0
    for i in range(digging_days_for_location):
        mined_gold_for_the_day = float(input())
        total_mined_gold += mined_gold_for_the_day
    average = total_mined_gold / digging_days_for_location
    if average >= expected_gold:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {expected_gold - average:.2f} gold.")

