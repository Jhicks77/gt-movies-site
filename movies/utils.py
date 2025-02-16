import requests
from django.core.files.base import ContentFile
from .models import Movie

def get_movie_image(movie, image_path):
    image_url = f"https://image.tmdb.org/t/p/w500{image_path}"
    image_response = requests.get(image_url)

    if image_response.status_code != 200:
        return False

    movie.image.save(f"{movie.name.replace("/", "")}.jpg", ContentFile(image_response.content), save=True)

    return True


def create_new_movie(movie_info):
    movie = Movie()
    movie.name = movie_info['title']
    movie.description = movie_info['overview']
    movie.price = 5
    if get_movie_image(movie, movie_info['poster_path']):
        movie.save()


def add_movies_to_database(search_term):
    """
    calculate_cart_total() correctly calculates the total value
    of the items contained in the cart dictionary
    """
    API_KEY = "8fbc775c17dfdc7c290908ec1ecbeaec"
    BASE_URL = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": search_term,
        "include_adult": "false",
        "language": "en-US",
        "page": 1
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return

    movie_list = response.json()['results']

    movie_list.sort(key=lambda movie: -float(movie.get('popularity', 0)))
    movie_list = movie_list[:4]
    for movie in movie_list:
        needed_keys = ['title', 'overview', 'poster_path']

        # if the dictionary isn't missing info about the movie, and we don't already have it in the db
        if all(key in movie.keys() for key in needed_keys) and\
                movie['title'] not in Movie.objects.values_list("name", flat=True):
            create_new_movie(movie)
            # then add it to the db

