from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
 path('signup', views.signup, name='accounts.signup'),
 path('login/', views.login, name='accounts.login'),
 path('logout/', views.logout, name='accounts.logout'),
 path('orders/', views.orders, name='accounts.orders'),
path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]