lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_sword = 0
broken_shield = 0
broken_armor = 0
broken_helmet = 0

for lost_game in range(1, lost_fights_count + 1):
    if lost_game % 2 == 0:
        broken_helmet += 1
    if lost_game % 3 == 0:
        broken_sword += 1
    if lost_game % 2 == 0 and lost_game % 3 == 0:
        broken_shield += 1
        if broken_shield % 2 == 0:
            broken_armor += 1
expenses = (broken_sword * sword_price) \
           + (broken_shield * shield_price) \
           + (broken_armor * armor_price) \
           + (broken_helmet * helmet_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")