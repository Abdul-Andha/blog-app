from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.article_list) #home page of the articles app
]
