from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 



class UserRegisterationForm(UserCreationForm): 
	email = forms.EmailField() 
	unique_together = ('email',)

	class Meta: 
		model= User
		fields=['username', 'email', 'password1', 'password2']
