month = input()
spend_hours = int(input())
peoples_count = int(input())
time_of_the_day = input()
tax_pur_hour = 0
if time_of_the_day == 'day':
    if month == 'march' or month == 'april' or month == 'may':
        price = 10.50
        tax_pur_hour += price
    elif month == 'june' or month == 'july' or month == 'august':
        price = 12.60
        tax_pur_hour += price
if time_of_the_day == 'night':
    if month == 'march' or month == 'april' or month == 'may':
        price = 8.40
        tax_pur_hour += price
    elif month == 'june' or month == 'july' or month == 'august':
        price = 10.20
        tax_pur_hour += price


if peoples_count >= 4:
    tax_pur_hour *= 0.90

if spend_hours >= 5:
    tax_pur_hour *= 0.50
hall_price = tax_pur_hour * peoples_count * spend_hours

print(f"Price per person for one hour: {tax_pur_hour:.2f}")
print(f"Total cost of the visit: {hall_price:.2f}")
