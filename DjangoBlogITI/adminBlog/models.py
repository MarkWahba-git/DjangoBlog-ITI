from django.db import models
from django.contrib.auth.models import User

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
