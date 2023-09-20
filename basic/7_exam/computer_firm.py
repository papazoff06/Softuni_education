model_computers_count = int(input())

sales = 0
sales_count = 0
rating_sum = 0


for n in range(model_computers_count):
    number = int(input())

    rating = number % 10
    possible_sales = number // 10

    if rating == 2:
        sales = possible_sales * 0
        sales_count += sales
        rating_sum += rating
    elif rating == 3:
        sales = possible_sales / 2
        sales_count += sales
        rating_sum += rating
    elif rating == 4:
        sales = possible_sales * 0.70
        sales_count += sales
        rating_sum += rating
    elif rating == 5:
        sales = possible_sales * 0.85
        sales_count += sales
        rating_sum += rating
    elif rating == 6:
        sales = possible_sales
        sales_count += sales
        rating_sum += rating
avarage = rating_sum / model_computers_count
print(f'{sales_count:.2f}')
print(f'{avarage:.2f}')
