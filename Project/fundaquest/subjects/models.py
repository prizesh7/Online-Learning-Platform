from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone


class Subject(models.Model):
	subject_id = models.AutoField(primary_key=True)
	subject_name = models.CharField(max_length=100)
	semester = models.IntegerField()
	description = models.CharField(max_length=500, blank=True)
	credit = models.FloatField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return (self.subject_name)

	def __repr__(self):
		return self.subject_name

	def get_absolute_url(self):
		return reverse("subjects-home")

class Topic(models.Model):
	topic_id = models.AutoField(primary_key=True)
	topic_name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	data = models.CharField(max_length=1000, blank=True)
	image = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.topic_name

	def get_absolute_url(self):
		return reverse("topic-list")
