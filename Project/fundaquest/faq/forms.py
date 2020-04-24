from django import forms
from users.models import Student
from subjects.models import Subject
from .models import Query

class QueryForm(forms.ModelForm):
	class Meta:
		model = Query
		fields = ('subject','desp','student')
		student = Student.objects.all()
		subject = Subject.objects.all()
