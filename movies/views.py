from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
movies = [ {
        'id': 1, 'name': 'Inception', 'price': 12,
        'description': 'A mind-bending heist thriller.'
    },
    {
        'id': 2, 'name': 'Avatar', 'price': 13,
        'description': 'A journey to a distant world and the battle for resources.'
    },
    {
        'id': 3, 'name': 'Batman', 'price': 14,
        'description': 'A Gotham vigilante faces the Joker.'
    },
    {
        'id': 4, 'name': 'Titanic', 'price': 11,
        'description': 'A love story set against the backdrop of the sinking Titanic.',
},
]

def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

#def show(request, id):
    #return HttpResponse(f'placeholder view for movie number {id}')
def show(request, id):
    movie = movies[id - 1]
    template_data = {}
    template_data['title'] = movie['name']
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
