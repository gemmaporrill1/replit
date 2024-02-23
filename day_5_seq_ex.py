# movie data
movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
]

# Task 1 - Find average for all - map, filter, all, ...

# Dont use for loop or List comp

#task 1
# output all movie titles

# movie_titles = map(lambda x: x["title"], movies)
# title_list = list(movie_titles)
# print(title_list)

# #task 1.1 create a list with average for all - seq methods
# # map, filter, all ...
# # don't use for loop or list comp

# average_rating = map(lambda x: sum(x["ratings"]) / len(x['ratings']), movies)
# rating_list = list(average_rating)
# print(rating_list)

#task 1.2 find average for all - map, filter, all
# copy
# movies = [

#     {"title": "Inception", "ratings": [5, 4, 5, 4, 5], "average_rating": 4.6},

#     {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4], "average_rating": 4.6},

#     {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4], "average_rating": 3.8},

#     {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5], "average_rating": 5.0},

#     {"title": "Memento", "ratings": [4, 5, 4, 5, 4], "average_rating": 4.4},

# ]


def find_avg(movie):
  return sum(movie['ratings']) / len(movie['ratings'])


movies_avg_ratings = list(map(
    lambda movie: {
        **movie, "average_rating": find_avg(movie)
    }, movies))
# print(movies_avg_ratings)

# copy with ** and give new parameter

# task 2
# max
# clue: max(key=fn)
# find top rated movie

# def find_avg(movie):
#   return sum(movie['ratings']) / len(movie['ratings'])

# top_movie = max(movies, key = lambda movie: average_rating)
# print(top_movie)

# top_movie = max(movies_avg_ratings, key=lambda movie: find_avg(movie))
# print(top_movie['title'])

#task 3
# movies with ratings more than 4.6

top_movie = list(filter(lambda movie: movie["average_rating"] >= 4.6, movies_avg_ratings))
printed_list = map(lambda x: x['title'], top_movie)
print(list(printed_list))


#task 4 -> discuss on Monday
# order by the rating 

ordered_rating = list(sorted(movies_avg_ratings, key=lambda movie: movie["average_rating"], reverse=True))
titles = map(lambda x: x['title'], ordered_rating)
print(list(titles))