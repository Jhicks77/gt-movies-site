from django.test import TestCase
from movies.models import Movie
from .utils import calculate_cart_total
import random

# class CartCalculatorTests(TestCase):
#     def test_calculate_cart_total_works(self):
#         print("hi")
#         test_cart = {}
#
#         running_combined_cost = 0
#
#         movies_in_cart = []
#         for _ in range(100):
#             random_movie = random.choice(Movie.objects.all())
#             random_movie_id = random_movie.id
#             random_movie_price = random_movie.price
#             random_quantity = random.randint(1, 10)
#
#             movies_in_cart.append(random_movie)
#             test_cart[random_movie_id] = random_quantity
#             running_combined_cost += random_movie_price * random_quantity
#
#         calculated_total = calculate_cart_total(test_cart, movies_in_cart)
#         self.assertIs(calculated_total, running_combined_cost)
#
#
