budget = float(input())
season = input()
vacantion_place = 0


if 0 <= budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacantion_place = 'Camp'
        budget *= 0.30
    elif season == 'winter':
        vacantion_place = 'Hotel'
        budget *= 0.70

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacantion_place = 'Camp'
        budget *= 0.40
    elif season == 'winter':
        vacantion_place = 'Hotel'
        budget *= 0.80

elif budget > 1000:
    destination = 'Europe'
    vacantion_place = 'Hotel'
    if season == 'summer' \
        or season == 'winter':
        budget *= 0.90
print(f'Somewhere in {destination}')
print(f'{vacantion_place} - {budget:.2f}')


