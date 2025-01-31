from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('placeholder movies index view')

def show(request, id):
    return HttpResponse(f'placeholder view for movie number {id}')

#login required
def create_review(request, id):
    return HttpResponse(f'placeholder view for reviewing movie number {id}')

#login required
def edit_review(request, id, review_id):
    return HttpResponse(f'placeholder view for editing review number {review_id} of movie number {id}')

#login required
def delete_review(request, id, review_id):
    return HttpResponse(f'placeholder view for deleting review number {review_id} of movie number {id}')
