from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        template_data['form'] = UserCreationForm()
        return render(request, 'accounts/signup.html',
                      {'template_data': template_data})


def login(request):
    return HttpResponse('placeholder account login view')


def logout(request):
    return HttpResponse('placeholder account logout view')

#login required
def orders(request):
    return HttpResponse('placeholder view for viewing the orders of an account')