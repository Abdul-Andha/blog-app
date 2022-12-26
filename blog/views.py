from django.http import HttpResponse
from django.shortcuts import render

def about(req):
  return render(req, 'about.html')
  #return HttpResponse("about")

def home(req):
  return render(req, 'index.html')
  #return HttpResponse("home")