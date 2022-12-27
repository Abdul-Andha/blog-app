from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(req):
  if req.method == 'POST':
    form = UserCreationForm(req.POST) #filled out form to validate and save  
    if form.is_valid():
      form.save()
      #log in
      return redirect('articles:list')  
  else:
    form = UserCreationForm() #blank form to render to the user
  
  return render(req, 'accounts/signup.html', {'form': form})