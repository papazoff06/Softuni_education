cars_for_taxed = input().split('>>')
total_taxes = 0
for car in cars_for_taxed:
    current_car = car.split(' ')
    car_type = current_car[0]
    tax_years = int(current_car[1])
    kilometers = int(current_car[2])
    if car_type == 'family':
        family_tax = 50 - tax_years * 5 + (kilometers // 3000 * 12)
        total_taxes += family_tax
        print(f"A {car_type} car will pay {family_tax:.2f} euros in taxes.")
    elif car_type == 'heavyDuty':
        heavy_duty_tax = 80 - tax_years * 8 + (kilometers // 9000 * 14)
        total_taxes += heavy_duty_tax
        print(f"A {car_type} car will pay {heavy_duty_tax:.2f} euros in taxes.")
    elif car_type == 'sports':
        sports_tax = 100 - tax_years * 9 + (kilometers // 2000 * 18)
        total_taxes += sports_tax
        print(f"A {car_type} car will pay {sports_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")
        continue

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")

