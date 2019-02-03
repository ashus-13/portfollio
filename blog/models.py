from django.db import models

# Create your models here.
class Blog(models.Model):
	place = models.CharField(max_length=30)
	date = models.DateTimeField()
	activity = models.TextField()