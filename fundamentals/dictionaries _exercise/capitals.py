country_names = input().split(', ')
capital_cities = input().split(', ')

some_dict = dict(zip(country_names, capital_cities))
for country_names, capital_cities in some_dict.items():
    print(f'{country_names} -> {capital_cities}')