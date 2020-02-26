from django.contrib.auth import login, authenticate
from django.contrib.auth.views import (
    LoginView,
)
from .forms import UserRegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/djangoBlog/home')
    else:
        form = UserRegisterationForm()
    return render(request, 'signup.html',{'form': form})

def home(request): 
	return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("/djangoBlog/home")
	
    else:
        form= AuthenticationForm()
    return render(request,'login_form.html',{'form':form})

def confirm_login_allowed(self, user):
        
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )



