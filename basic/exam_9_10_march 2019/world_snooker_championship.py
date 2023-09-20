# От конзолата се четат 3 реда:
# 1.	Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
# 2.	Вид на билета – текст - “Standard”, “Premium” или “VIP”
# 3.	Брой билети – цяло число в интервала [1 … 30]
# 4.	Снимка с трофея – символ – 'Y' (да) или 'N' (не)
stage = input()
kind_of_ticket = input()
count_of_tickets = int(input())
picture = input()
ticket_price = 0
if stage == 'Quarter final':
    if kind_of_ticket == 'Standard':
        ticket_price += 55.50
    elif kind_of_ticket == 'Premium':
        ticket_price += 105.20
    elif kind_of_ticket == 'VIP':
        ticket_price += 118.90
elif stage == 'Semi final':
    if kind_of_ticket == 'Standard':
        ticket_price += 75.88
    elif kind_of_ticket == 'Premium':
        ticket_price += 125.22
    elif kind_of_ticket == 'VIP':
        ticket_price += 300.40
elif stage == 'Final':
    if kind_of_ticket == 'Standard':
        ticket_price += 110.10
    elif kind_of_ticket == 'Premium':
        ticket_price += 160.66
    elif kind_of_ticket == 'VIP':
        ticket_price += 400
final_price = count_of_tickets * ticket_price
if final_price <= 2500:
    final_price = final_price
    if picture == 'Y':
        final_price += count_of_tickets * 40
elif 2500 < final_price <= 4000:
    final_price *= 0.90
    if picture == 'Y':
        final_price += count_of_tickets * 40
elif final_price > 4000:
    final_price *= 0.75
    if picture == 'Y':
        final_price = final_price
print(f'{final_price:.2f}')
