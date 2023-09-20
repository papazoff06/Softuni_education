length_thank = int(input())
width_thank = int(input())
height_thank = int(input())
percent_other_staff = float(input())

volume_thank = (length_thank * width_thank * height_thank) * 0.001
water_in_thank = volume_thank * (100 - percent_other_staff) / 100
print(water_in_thank)