from django.db import models
from django.contrib.auth.models import User


class Moment(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='moments')
	owner = models.ForeignKey(User, related_name='moments')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class MomentsCollection(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	cover_image = models.ForeignKey(Moment, related_name='cover_image_for')
	moments = models.ManyToManyField(Moment, related_name='moment_collections')
	owner = models.ForeignKey(User, related_name='moment_collections')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
