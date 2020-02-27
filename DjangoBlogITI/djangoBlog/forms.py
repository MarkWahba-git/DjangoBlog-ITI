from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from adminBlog.models import Post,Tags,Comment,reply



class UserRegisterationForm(UserCreationForm): 
	email = forms.EmailField() 
	unique_together = ('email',)

	class Meta: 
		model= User
		fields=['username', 'email', 'password1', 'password2']



class postform(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['title','post_date','image','content','user_id','category_id','tag_name']



class commentform(forms.ModelForm):

	class Meta:
		model= Comment
		fields=['comment_content']




		



