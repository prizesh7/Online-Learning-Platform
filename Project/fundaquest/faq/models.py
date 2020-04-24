from django.db.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from users.models import Student,Teacher
from subjects.models import Subject
from django.urls import reverse





class Query(models.Model):
	qid= AutoField(primary_key = True)
	student = ForeignKey(Student, on_delete=models.CASCADE, null=True)
	subject= ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	desp = TextField(max_length=1000, blank=True)

	def get_absolute_url(self):
		return reverse("query-home")



class Answer(models.Model):
	aid= AutoField(primary_key = True)
	teacher = ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
	subject= ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	desp = TextField(max_length=1000, blank=True)
	question= ForeignKey(Query, on_delete=models.CASCADE, null=True)
