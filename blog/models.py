from django.db import models

# Create your models here.
class Blog(models.Model):
	place = models.CharField(max_length=30)
	date = models.DateTimeField()
	activity = models.TextField()

	def __str__(self):
		return self.place

	def date_new(self):
		return self.date.strftime('%b %e %Y')

	def activity_new(self):
		return self.activity[:100]		