# 1.	Рекордът в секунди – реално число в интервала [0.00 … 100000.00]
# 2.	Разстоянието в метри – реално число в интервала [0.00 … 100000.00]
# 3.	Времето в секунди, за което изкачва 1 м. – реално число в интервала [0.00 … 1000.00
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

georgi_time = distance_in_meters * time_in_seconds_for_one_meter
delay_time = (distance_in_meters // 50) * 30
georgi_with_delay_time = georgi_time + delay_time

if georgi_with_delay_time < record_in_seconds:
    print(f" Yes! The new record is {georgi_with_delay_time:.2f} seconds.")
else:
    print(f"No! He was {georgi_with_delay_time - record_in_seconds:.2f} seconds slower.")

