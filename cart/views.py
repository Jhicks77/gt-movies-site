from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("placeholder index view for cart")
def add(request, id):
    return HttpResponse(f'placeholder view for adding movie number {id} to your cart')

def clear(request):
    return HttpResponse('placeholder view for clearing cart')

#login required
def purchase(request):
    return HttpResponse('placeholder view for making a purchase')