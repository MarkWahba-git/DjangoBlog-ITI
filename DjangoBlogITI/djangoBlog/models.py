from django.db import models

# Create your models here.

class category(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name
class forbidden_words(models.Model):
	name=models.CharField(max_length=40)
	def __str__(self):
		return self.name
