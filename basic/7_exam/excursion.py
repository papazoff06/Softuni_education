# 1.	Броят на хората в групата – цяло число в интервала [0 … 50]
# 2.	Броят на нощувките – цяло число в интервала [0 … 2000]
# 3.	Броят на картите за транспорт – цяло число в интервала [0… 2000]
# 4.	Броят на билетите за музеи – цяло число в интервала
night_price = 20
transport_card_price = 1.60
ticket_price = 6


peoples_count = int(input())
nights_count = int(input())
transport_cards_count = int(input())
tickets_count = int(input())

whole_nights_expencese = peoples_count * nights_count * night_price
whole_transport_expencese = peoples_count * transport_cards_count * transport_card_price
whole_ticket_expencese = peoples_count * tickets_count * ticket_price

final_price = (whole_ticket_expencese + whole_transport_expencese + whole_nights_expencese) * 1.25

print(f'{final_price:.2f}')
