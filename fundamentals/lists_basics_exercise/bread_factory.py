day_events = input().split('|')
energy = 100
coins = 100
is_closed = False
for i in day_events:
    event = i.split('-')
    event_name = event[0]
    number = int(event[1])
    if event_name == 'rest':
        if energy + number <= 100:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
        else:
            energy += 100 - energy
            print(f"You gained {100 - energy} energy.")
            print(f"Current energy: {energy}.")
    elif event_name == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


