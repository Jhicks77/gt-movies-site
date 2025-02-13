from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies=Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

#def show(request, id):
    #return HttpResponse(f'placeholder view for movie number {id}')
def show(request, id):
    movie = Movie.objects.get(id=id)
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(request, 'movies/show.html',{'template_data': template_data})

@login_required
def create_review(request, id):
    return HttpResponse(f'placeholder view for reviewing movie number {id}')

@login_required
def edit_review(request, id, review_id):
    return HttpResponse(f'placeholder view for editing review number {review_id} of movie number {id}')

@login_required
def delete_review(request, id, review_id):
    return HttpResponse(f'placeholder view for deleting review number {review_id} of movie number {id}')
