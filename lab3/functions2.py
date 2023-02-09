movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


def is_highly_rated(movie):
    return movie["imdb"] > 5.5

def highly_rated_movies(movies):
    return [movie for movie in movies if is_highly_rated(movie)]

def by_category(category, movies):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb_score(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

def average_category_score(category, movies):
    movies_by_category = by_category(category, movies)
    return average_imdb_score(movies_by_category)



# 1
# print(is_highly_rated(movies[0]))

# #2
# highly_rated = highly_rated_movies(movies)
# print("Highly rated movies:")
# for movie in highly_rated:
#     print(movie["name"], movie["imdb"])

# # 3
# comedy_movies = by_category("Comedy", movies)
# print("Comedy movies:")
# for movie in comedy_movies:
#     print(movie["name"], movie["imdb"])


# # 4
# print("Average IMDB score:", average_imdb_score(movies))

# # 5 'Romance'
# print("Average IMDB score for Romance:", average_category_score("Romance", movies))

