from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('placeholder home index view')

def about(request):
    return HttpResponse('placeholder home about view')