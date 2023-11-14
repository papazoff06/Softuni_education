days_adventure = int(input())
number_of_players = int(input())
groups_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
whole_water = number_of_players * water_per_day_per_person * days_adventure
whole_food = number_of_players * food_per_day_per_person * days_adventure

for day in range(1, days_adventure + 1):
    energy_lost = float(input())
    groups_energy -= energy_lost
    if groups_energy <= 0:
        print(f"You will run out of energy. You will be left with {whole_food:.2f} food and {whole_water:.2f} water.")
        break
    if day % 2 == 0:
        groups_energy += groups_energy * 0.05
        whole_water -= whole_water * 0.3
    if day % 3 == 0:
        whole_food -= whole_food / number_of_players
        groups_energy *= 1.1
if groups_energy > 0:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")


