from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.utils import timezone
from users.models import Teacher
from subjects.models import Subject,Topic
from fundaquest.settings import MEDIA_URL

# Create your models here.

class File(models.Model):
	file_id=models.AutoField(primary_key=True)
	file = models.FileField(upload_to='static')
	topic= models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
	date=models.DateTimeField(default=timezone.now)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
