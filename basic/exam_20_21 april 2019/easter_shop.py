# •	На първи ред - Началното количество яйца в магазина - цяло число в интервала [1… 10000]
# •	След това поредица от два реда (до получаване на команда "'Close'" или при заявка за купуване на повече от наличните в магазина яйца) :
# o	Команда за купуване или допълване на яйца в магазина – текст ("Buy" или "Fill")
# o	Брой на яйца, които да бъдат купени или допълнени в магазина – цяло число в интервала
starting_eggs_in_yhe_store = int(input())
eggs_in_store = starting_eggs_in_yhe_store
saled_eggs = 0
command = input()
while command != 'Close':
    eggs_buy_or_fill_in_store = command
    count_of_eggs = int(input())
    if eggs_buy_or_fill_in_store == 'Buy':
        if eggs_in_store < count_of_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs_in_store}.")
            break
        saled_eggs += count_of_eggs
        eggs_in_store -= count_of_eggs

    elif eggs_buy_or_fill_in_store == 'Fill':
        eggs_in_store += count_of_eggs
    command = input()
if command == 'Close':
    print('Store is closed!')
    print(f"{saled_eggs} eggs sold.")


