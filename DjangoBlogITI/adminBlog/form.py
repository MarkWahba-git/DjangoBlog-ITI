from django import forms
from django.contrib.auth.models import User
from adminBlog.models import category,forbidden_words
class usr_form(forms.ModelForm):
	class Meta:
		model=User
		fields=('username','email','password','is_staff')

class word_form(forms.ModelForm):
	class Meta:
		model=forbidden_words
		fields=('name',)

class usr_block(forms.ModelForm):
	class Meta:
		model=User
		fields=('is_active',)


class cat_form(forms.ModelForm):
	class Meta:
		model=category
		fields=('name',)
