from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import Student,Teacher,TeacherManager
from subjects.models import Subject


class UserRegisterForm(UserCreationForm):
	'''first_name = forms.CharField()
	last_name = forms.CharField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = forms.CharField(validators=[phone_regex])
	city = forms.CharField()
	dob = forms.DateField()
	department = forms.CharField()
	semester = forms.IntegerField()
	image = forms.ImageField()'''

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'city','phone', 'dob','department','semester','image']


class TeacherForm(forms.ModelForm):

	class Meta:
		model = Teacher
		fields = ['first_name', 'last_name', 'city', 'phone','department','exp','image']

# class TeacherModelForm(forms.ModelForm):
#
# 	class Meta:
# 		model = TeacherManager
# 		fields = ['subject']
# 		subject = forms.ModelChoiceField(queryset=Subject.objects.order_by('subjects_name').values_list('subject_name').distinct())
