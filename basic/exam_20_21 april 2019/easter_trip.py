# •	Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
# •	Втори ред - дати, през които си е резервирала екскурзията - текст  с възможности "21-23",
# "24-27" или "28-31"
# •	Трети ред - брой нощувки - цяло число в интервала [1… 100]
destination = input()
dates_of_the_trip = input()
nights_count = int(input())
price = 0

if destination == 'France':
    if dates_of_the_trip == '21-23':
        price = 30
    elif dates_of_the_trip == '24-27':
        price = 35
    elif dates_of_the_trip == '28-31':
        price = 40
elif destination == 'Italy':
    if dates_of_the_trip == '21-23':
        price = 28
    elif dates_of_the_trip == '24-27':
        price = 32
    elif dates_of_the_trip == '28-31':
        price = 39
elif destination == 'Germany':
    if dates_of_the_trip == '21-23':
        price = 32
    elif dates_of_the_trip == '24-27':
        price = 37
    elif dates_of_the_trip == '28-31':
        price = 43
trip_price = nights_count * price
print(f"Easter trip to {destination} : {trip_price:.2f} leva.")