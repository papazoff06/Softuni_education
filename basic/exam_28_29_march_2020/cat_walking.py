minutes_walk_per_day = int(input())
count_of_walks_per_day = int(input())
taken_calories_per_day = int(input())
whole_cat_calories_per_day = minutes_walk_per_day * count_of_walks_per_day * 5
if whole_cat_calories_per_day >= taken_calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {whole_cat_calories_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {whole_cat_calories_per_day}.")

