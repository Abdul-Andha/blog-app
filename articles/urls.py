from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.article_list, name='list'), #home page of the articles app
  path('<slug:slug>', views.article_detail, name="detail") #specific article page
]
