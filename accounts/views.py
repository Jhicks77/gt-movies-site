from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
                      {'template_data': template_data})

    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST,
                error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                      {'template_data': template_data})


def login(request):
    return HttpResponse('placeholder account login view')


def logout(request):
    return HttpResponse('placeholder account logout view')

#login required
def orders(request):
    return HttpResponse('placeholder view for viewing the orders of an account')