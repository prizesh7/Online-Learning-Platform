from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.utils import timezone
from subjects.models import Subject,Topic
from users.models import Teacher
from django.urls import reverse

class Article(models.Model):
	article_id = models.AutoField(primary_key=True)
	date = models.DateTimeField(default=timezone.now)
	data = models.TextField(max_length=1000)
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.topic.topic_name

	def get_absolute_url(self):
		return reverse("articles-home")
