from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.utils import timezone
from subjects.models import Subject,Topic
from users.models import Teacher

class Video(models.Model):
	video_id=models.AutoField(primary_key=True)
	video= models.FileField(upload_to='videos/', null=True, verbose_name="")
	topic= models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
	date=models.DateTimeField(default=timezone.now)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
