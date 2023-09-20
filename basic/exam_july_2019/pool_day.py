import math
peoples_count = int(input())
entry_fee = float(input())
sun_bed_price = float(input())
umbrella_price = float(input())

umbrella_count = math.ceil(peoples_count * 0.50)
sun_bed_count = math.ceil(peoples_count * 0.75)

price = (peoples_count * entry_fee) + (umbrella_count * umbrella_price) + (sun_bed_count * sun_bed_price)
print(f"{price:.2f} lv.")
