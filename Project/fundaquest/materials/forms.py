from django import forms
from .models import File
from users.models import Teacher
from subjects.models import Subject, Topic

class FileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ('topic', 'file', 'teacher', 'subject')
		topic = forms.ModelChoiceField(queryset=Topic.objects.all())
		teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
		subject = forms.ModelChoiceField(queryset=Subject.objects.all())
		file=forms.FileField()
