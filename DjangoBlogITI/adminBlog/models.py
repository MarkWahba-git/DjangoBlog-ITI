from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class category(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name

class forbidden_words(models.Model):
	name=models.CharField(max_length=40)
	def __str__(self):
		return self.name

class subscribe(models.Model):
	category_id=models.ForeignKey(category,on_delete=models.DO_NOTHING)
	user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)


class Tags (models.Model):
	tag_name=models.CharField(max_length=50)

	def __str__(self):
		return self.tag_name	


class Post (models.Model):
	title= models.CharField(max_length=100)
	post_date=models.DateTimeField(default=timezone.now)
	post_update=models.DateTimeField(auto_now=True)
	image=models.FileField( blank=True)
	content=models.TextField()
	user_id=models.ForeignKey(User, on_delete=models.CASCADE)
	category_id=models.ForeignKey(category,on_delete=models.DO_NOTHING)
	tag_name=models.ManyToManyField(Tags)

	def __str__(self):
		return self.title


	def __str__(self):
		return self.title 

	class Meta:
		ordering = ('-post_date', )


class Comment (models.Model):
	post_name=models.ForeignKey(Post, on_delete=models.CASCADE)
	user_id=models.ForeignKey(User, on_delete=models.CASCADE,default='1')
	comment_content=models.TextField(max_length=100)


	def __str__(self):
		return self.comment_content	

class reply(models.Model):
	reply_content=models.TextField(max_length=100)
	user_id=models.ForeignKey(User, on_delete=models.CASCADE)
	comment_id=models.ForeignKey(Comment , on_delete=models.DO_NOTHING)

	



