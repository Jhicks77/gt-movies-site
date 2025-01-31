from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def signup(request):
    return HttpResponse('placeholder account signup view')


def login(request):
    return HttpResponse('placeholder account login view')


def logout(request):
    return HttpResponse('placeholder account logout view')

#login required
def orders(request):
    return HttpResponse('placeholder view for viewing the orders of an account')