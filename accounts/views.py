from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(req):
  if req.method == 'POST':
    form = UserCreationForm(req.POST) #filled out form to validate and save  
    if form.is_valid():
      user = form.save()
      login(req, user)
      return redirect('articles:list')  
  else:
    form = UserCreationForm() #blank form to render to the user
  
  return render(req, 'accounts/signup.html', {'form': form})

def login_view(req):
  if req.method == 'POST':
    form = AuthenticationForm(data=req.POST)
    if form.is_valid(): #log in the user
      user = form.get_user()
      login(req, user)

      if 'next' in req.POST:
        return redirect(req.POST.get('next'))        
      else:
        return redirect('articles:list')
  else:
    form = AuthenticationForm() 

  next = None
  if req.GET.get('next'):
    next = req.GET.get('next')
  return render(req, 'accounts/login.html', {'form': form, 'next': next})
  

def logout_view(req):
  if req.method == 'POST':
    logout(req)
    return redirect('articles:list')