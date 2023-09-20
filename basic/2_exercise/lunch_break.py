from math import ceil
movie_name = (input())
movie_lenght = int(input())
break_lenght = int(input())
# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка,
# а времето за отдих ще бъде 1/4 от времето за почивка.
lunch_time = break_lenght / 8
rest_time = break_lenght / 4

time_for_movie = break_lenght - (lunch_time + rest_time)
if time_for_movie >= movie_lenght:
    print(f"You have enough time to watch {movie_name} and left with "
          f"{ceil(time_for_movie - movie_lenght)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, "
          f"you need {ceil(movie_lenght - time_for_movie)} more minutes.")