number_of_cars = int(input())
dict_with_cars = {}
for i in range(number_of_cars):
    current_command = input().split('|')
    car = current_command[0]
    mileage = int(current_command[1])
    fuel = int(current_command[2])
    dict_with_cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while command != 'Stop':
    given_command = command.split(' : ')
    if given_command[0] == 'Drive':
        car = given_command[1]
        distance = int(given_command[2])
        given_fuel = int(given_command[3])
        if given_fuel > dict_with_cars[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            dict_with_cars[car]['fuel'] = dict_with_cars[car]['fuel'] - given_fuel
            dict_with_cars[car]['mileage'] = dict_with_cars[car]['mileage'] + distance
            print(f"{car} driven for {distance} kilometers. {given_fuel} liters of fuel consumed.")
        if dict_with_cars[car]["mileage"] > 100_000:
            print(f"Time to sell the {car}!")
            del dict_with_cars[car]

    elif given_command[0] == 'Refuel':
        car = given_command[1]
        fuel = int(given_command[2])
        if dict_with_cars[car]['fuel'] + fuel > 75:
            print(f"{car} refueled with {75 - dict_with_cars[car]['fuel']} liters")
            dict_with_cars[car]['fuel'] = 75

        else:
            dict_with_cars[car]['fuel'] = dict_with_cars[car]['fuel'] + fuel
            print(f"{car} refueled with {fuel} liters")

    elif given_command[0] == 'Revert':
        car = given_command[1]
        kilometers = int(given_command[2])
        dict_with_cars[car]['mileage'] = dict_with_cars[car]['mileage'] - kilometers
        if dict_with_cars[car]['mileage'] < 10_000:
            dict_with_cars[car]['mileage'] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()
for key, value in dict_with_cars.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")

