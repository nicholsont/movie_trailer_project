import media
import fresh_tomatoes

# Instantiation of the Movie class
# Params: title, duration, rating, poster_image_url, trailer_url
fifth_element = media.Movie(
    "Fifth Element",
    "126 min",
    "PG-13",
    "http://www.crankycritic.com/archive/posters/5thelement.jpg",
    "https://www.youtube.com/watch?v=fQ9RqgcR24g"
)

lion_king = media.Movie(
    "Lion King",
    "88 min",
    "G",
    "https://images-na.ssl-images-amazon.com/images/I/418g2jo7fBL._AC_UL320_SR216,320_.jpg",  # noqa
    "https://www.youtube.com/watch?v=4sj1MT05lAA"
)

kill_bill = media.Movie(
    "Kill Bill: Vol. 1",
    "111 min",
    "R",
    "https://i.ebayimg.com/images/g/ItQAAOSwDtpZbYx4/s-l300.jpg",
    "https://www.youtube.com/watch?v=7kSuas6mRpk"
)

django_unchained = media.Movie(
    "Django Unchained",
    "165 min",
    "R",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=eUdM9vrCbow"
)

thor_ragnarok = media.Movie(
    "Thor: Ragnarok",
    "130 min",
    "PG-13",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=ue80QwXMRHg"
)

guardians_of_the_galaxy = media.Movie(
    "Guardians of the Galaxy",
    "121 min",
    "PG-13",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=d96cjJhvlMA"
)

# Populate the movies array
movies = [
    fifth_element,
    lion_king,
    kill_bill,
    django_unchained,
    thor_ragnarok,
    guardians_of_the_galaxy
]

# Write and open the movie trailer html file
fresh_tomatoes.open_movies_page(movies)
