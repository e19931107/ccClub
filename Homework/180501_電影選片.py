first_movie_name = input()
first_movie_imdb = float([str(i) for i in input().split(':')][-1])
first_movie_type = [str(i) for i in input().split()]
second_movie_name = input()
second_movie_imdb = float([str(i) for i in input().split(':')][-1])
second_movie_type = [str(i) for i in input().split()]

type = {"Fantasy": 10,
        "Drama": 9,
        "Action": 8,
        "Thriller": 7,
        "Comedy": 6,
        "Crime": 5,
        "History": 4,
        "Romance": 3,
        "Adventure": 2,
        "Biography": 1}

movie = {first_movie_name:first_movie_imdb,second_movie_name:second_movie_imdb}

for i in first_movie_type:
    movie[first_movie_name] = movie[first_movie_name] + type[i]
for i in second_movie_type:
    movie[second_movie_name] = movie[second_movie_name] + type[i]

if movie[first_movie_name] > movie[second_movie_name]:
    print(first_movie_name)
elif movie[first_movie_name] < movie[second_movie_name]:
    print(second_movie_name)
else:
    print(first_movie_name, second_movie_name, sep = '\n')