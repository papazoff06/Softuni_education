
company_name = input()
adult_ticket_count = int(input())
kid_ticket_count = int(input())
adult_ticket_price = float(input())
service_price = float(input())



one_adult_ticket_price = adult_ticket_price + service_price
one_kid_ticket_price = (adult_ticket_price * 0.30) + service_price

whole_price = (adult_ticket_count * one_adult_ticket_price) + (kid_ticket_count * one_kid_ticket_price)
profit = whole_price * 0.20
print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')

