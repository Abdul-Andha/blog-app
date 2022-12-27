from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup_view, name='signup'), #signup page of the accounts app
  path('login/', views.login_view, name='login'), #login page of the accounts app
  path('logout/', views.logout_view, name='logout') 
]
