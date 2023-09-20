# •	Брой дни – цяло число в диапазона [1…30]
# •	Общо количество храна – реално число в диапазона [0.00…10000.00]
# След това за всеки ден се чете:
# o	Количество изядена храна от кучето – цяло число в диапазона [10…500]
# o	Количество изядена храна от котката – цяло число в диапазона [10…500]
count_of_days = int(input())
whole_food = float(input())
whole_eaten_dog_food = 0
whole_eaten_cat_food = 0
days_count = 0
biscuits = 0
for i in range(count_of_days):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())
    whole_eaten_dog_food += dog_eaten_food
    whole_eaten_cat_food += cat_eaten_food
    days_count += 1
    if days_count % 3 == 0:
        biscuits = (dog_eaten_food + cat_eaten_food) * 0.10
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(whole_eaten_dog_food + whole_eaten_cat_food) / whole_food * 100:.2f}% of the food has been eaten.")
print(f"{whole_eaten_dog_food / (whole_eaten_dog_food + whole_eaten_cat_food) * 100:.2f}% eaten from the dog.")
print(f"{whole_eaten_cat_food / (whole_eaten_dog_food + whole_eaten_cat_food) * 100:.2f}% eaten from the cat.")


