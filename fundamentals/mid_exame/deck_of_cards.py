list_of_cards = input().split(', ')
number = int(input())
for i in range(number):
    command = input().split(', ')
    if command[0] == 'Add':
        card_name = command[1]
        if card_name in list_of_cards:
            print("Card is already in the deck")
        else:
            list_of_cards.append(card_name)
            print("Card successfully added")
    elif command[0] == 'Remove':
        remove_card = command[1]
        if remove_card in list_of_cards:
            list_of_cards.remove(remove_card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == 'Remove At':
        card_index = int(command[1])
        if 0 <= card_index < len(list_of_cards):
            cart_fo_remove = list_of_cards[card_index]
            list_of_cards.pop(card_index, cart_fo_remove)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command[0] == 'Insert':
        idx = int(command[1])
        card_name = command[2]
        if 0 <= abs(idx) < len(list_of_cards):
            if card_name in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(idx, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(', '.join(list_of_cards))

