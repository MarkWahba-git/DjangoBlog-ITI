from django import forms
from django.contrib.auth.models import User
from adminBlog.models import category,forbidden_words,Post,Tags,Comment
from django.contrib.auth.forms import UserCreationForm 




class UserRegisterationForm(UserCreationForm): 
	email = forms.EmailField() 
	unique_together = ('email',)

	class Meta: 
		model= User
		fields=['username', 'email', 'password1', 'password2']



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
class usr_promote(forms.ModelForm):
	class Meta:
		model=User
		fields=('is_staff',)


class cat_form(forms.ModelForm):
	class Meta:
		model=category
		fields=('name',)


class postform(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['title','post_date','image','content','user_id','category_id','tag_name']



class commentform(forms.ModelForm):

	class Meta:
		model= Comment
		fields=['comment_content']

