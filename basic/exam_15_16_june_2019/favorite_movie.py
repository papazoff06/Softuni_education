import sys
command = input()
movie_count = 0
movie_sum = 0
best_score = - sys.maxsize
best_movie = ''

while command != 'STOP':
    movie = command
    movie_count += 1
    for letter in movie:
        if letter.isupper():
            movie_sum += ord(letter) - len(movie)
        elif letter.islower():
            movie_sum += ord(letter) - (2 * len(movie))
        else:
            movie_sum += ord(letter)
    if movie_sum > best_score:
        best_movie = command
        best_score = movie_sum
    movie_sum = 0
    if movie_count >= 7:
        print('The limit is reached.')
        break
    command = input()
print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")



