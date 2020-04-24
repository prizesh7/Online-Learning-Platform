from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from subjects.models import Subject
from django.core.validators import RegexValidator
from fundaquest.settings import MEDIA_URL

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null = True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	city = models.CharField(max_length=100, blank=True)
	dob = models.DateField(max_length=100, blank=True)
	department = models.CharField(max_length=100, blank=True)
	semester = models.IntegerField(default = 6)
	image = models.ImageField(upload_to = 'users', default = MEDIA_URL+'users/user.png' )

	def __str__(self):
		return (self.first_name + " " + self.last_name)

	def __repr__(self):
		return (self.first_name + " " + self.last_name)

class Teacher(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	city = models.CharField(max_length=100, blank=True)
	exp = models.CharField(max_length=100, blank=True)
	department = models.CharField(max_length=100, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	image = models.ImageField(upload_to = 'users', default = MEDIA_URL+'users/user.png' )

	def __str__(self):
		return (self.first_name + " " + self.last_name)

	def __repr__(self):
		return self.first_name + " " + self.last_name

class TeacherManager(models.Model):
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
