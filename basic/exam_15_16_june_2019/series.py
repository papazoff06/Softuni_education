# От конзолата се четат:
# •	Бюджет  - реално  число в интервала [10.0… 100.0]
# •	Брой сериали - n - цяло положително число в интервала [1… 10]
# За всеки сериал се четат по два реда:
# o	Име на сериал - текст
# o	Цена за сериал -  реално  число в интервала [1.0… 15.0]
budget = float(input())
count_of_movies = int(input())
for i in range(count_of_movies):
    movie_name = input()
    movie_price = float(input())
    if movie_name == 'Thrones':
        budget -= movie_price / 2
    elif movie_name =='Lucifer':
        budget -= 0.60 * movie_price
    elif movie_name == 'Protector':
        budget -= 0.70 * movie_price
    elif movie_name =='TotalDrama':
        budget -= 0.80 * movie_price
    elif movie_name == 'Area':
        budget -= 0.90 * movie_price
    else:
        budget -= movie_price
if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
