from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from movies.models import Movie
from .utils import calculate_cart_total

def index(request):
    cart_total = 0
    movies_in_cart = []
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if (movie_ids != []):
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)
        cart_total = calculate_cart_total(cart,movies_in_cart)
    template_data = {}
    template_data['title'] = 'Cart'
    template_data['movies_in_cart'] = movies_in_cart
    template_data['cart_total'] = cart_total
    return render(request, 'cart/index.html',
                  {'template_data': template_data})

def add(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})

    id = str(id) # allows for users to add the same movie to their cart multiple times
    if id not in cart: # otherwise this action would override their previous add-to-cart
        cart[id] = 0


    cart[id] = int(cart[id]) + int(request.POST['quantity']) # to handle any key type
    request.session['cart'] = cart
    return redirect('cart.index')

def clear(request):
    return HttpResponse('placeholder view for clearing cart')

@login_required
def purchase(request):
    return HttpResponse('placeholder view for making a purchase')