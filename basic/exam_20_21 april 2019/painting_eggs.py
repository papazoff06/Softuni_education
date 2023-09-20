# Първи ред – размер на яйцата – текст с възможности "Large", "Medium" или "Small"
#
# · Втори ред – цвят на яйцата – текст с възможности "Red", "Green" или "Yellow"
#
# · Трети ред – брой партиди – цяло число в интервала [1… 350
eggs_size = input()
eggs_color = input()
count_of_batches = int(input())
price = 0
if eggs_color == 'Red':
    if eggs_size == 'Large':
        price = 16
    elif eggs_size == 'Medium':
        price = 13
    elif eggs_size == "Small":
        price = 9
elif eggs_color == 'Green':
    if eggs_size == 'Large':
        price = 12
    elif eggs_size == 'Medium':
        price = 9
    elif eggs_size == "Small":
        price = 8
elif eggs_color == 'Yellow':
    if eggs_size == 'Large':
        price = 9
    elif eggs_size == 'Medium':
        price = 7
    elif eggs_size == "Small":
        price = 5
final_price = (count_of_batches * price) * 0.65
print(f"{final_price:.2f} leva.")
