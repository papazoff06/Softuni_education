# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
count_of_groups = int(input())
going_to_mussala = 0
going_to_montblanc = 0
going_to_kilimanjaro = 0
going_to_k2 = 0
going_to_everest = 0
for i in range(count_of_groups):
    people_in_group = int(input())
    if 1 <= people_in_group <= 5:
        going_to_mussala += people_in_group
    elif 6 <= people_in_group <= 12:
        going_to_montblanc += people_in_group
    elif 13 <= people_in_group <= 25:
        going_to_kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        going_to_k2 += people_in_group
    elif 41 <= people_in_group:
        going_to_everest += people_in_group
percentage_going_mussala = going_to_mussala / (going_to_mussala +
                                               going_to_montblanc + going_to_k2 +
                                               going_to_everest + going_to_kilimanjaro) * 100
percentage_going_montblanc = going_to_montblanc / (going_to_mussala +
                                               going_to_montblanc + going_to_k2 +
                                               going_to_everest + going_to_kilimanjaro) * 100
percentage_going_kilimanjaro = going_to_kilimanjaro / (going_to_mussala +
                                               going_to_montblanc + going_to_k2 +
                                               going_to_everest + going_to_kilimanjaro) * 100
percentage_going_k2 = going_to_k2 / (going_to_mussala +
                                               going_to_montblanc + going_to_k2 +
                                               going_to_everest + going_to_kilimanjaro) * 100
percentage_going_everest = going_to_everest / (going_to_mussala +
                                               going_to_montblanc + going_to_k2 +
                                               going_to_everest + going_to_kilimanjaro) * 100
print(f'{percentage_going_mussala:.2f}%')
print(f'{percentage_going_montblanc:.2f}%')
print(f'{percentage_going_kilimanjaro:.2f}%')
print(f'{percentage_going_k2:.2f}%')
print(f'{percentage_going_everest:.2f}%')



