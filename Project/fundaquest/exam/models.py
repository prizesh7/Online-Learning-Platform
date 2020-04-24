from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from subjects.models import Subject
from users.models import Teacher

class Question(models.Model):
	question_id=models.AutoField(primary_key=True)
	question= models.CharField(max_length=300)
	opt1= models.CharField(max_length=100)
	opt2= models.CharField(max_length=100)
	opt3= models.CharField(max_length=100)
	opt4= models.CharField(max_length=100,default=None)
	answer= models.CharField(max_length=100)
	hint=models.CharField(max_length=500)
	marks=models.IntegerField()
	difficulty=models.IntegerField()
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

	def get_absolute_url(self):
		return reverse("exam-home")
