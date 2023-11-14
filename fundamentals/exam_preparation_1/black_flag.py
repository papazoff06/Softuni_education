days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
whole_plunder = 0

for i in range(1, days_of_plunder + 1):
    whole_plunder += daily_plunder
    if i % 3 == 0:
        whole_plunder += daily_plunder * 0.5
    if i % 5 == 0:
        whole_plunder *= 0.7
if whole_plunder >= expected_plunder:
    print(f"Ahoy! {whole_plunder:.2f} plunder gained.")
else:
    percentage = 100 -(expected_plunder - whole_plunder) / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")

