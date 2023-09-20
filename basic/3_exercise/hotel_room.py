month = input()
nights_count = int(input())

studio_per_night = 0
apartment_per_night = 0
if month == 'May' or month == 'October':
    studio_per_night = 50
    apartment_per_night = 65
    if 7 < nights_count < 14:
        studio_per_night *= 0.95
    elif 14 < nights_count:
        studio_per_night *= 0.70

elif month == 'June' or month == 'September':
    studio_per_night = 75.20
    apartment_per_night = 68.70
    if nights_count > 14:
        studio_per_night *= 0.80

elif month == 'July' or month == 'August':
    studio_per_night = 76
    apartment_per_night = 77

if nights_count > 14:
    apartment_per_night *= 0.90

total_studio_price = studio_per_night * nights_count
total_apartment_price = apartment_per_night * nights_count
print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")

