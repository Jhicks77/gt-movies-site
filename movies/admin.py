from django.contrib import admin

from .models import Movie, Review
# Register your models here.
from .models import Movie

admin.site.register(Movie)
admin.site.register(Review)