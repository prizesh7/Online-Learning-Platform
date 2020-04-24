from django import forms
from .models import Subject, Topic

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = ('subject_name', 'semester', 'description', 'credit')

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ('topic_name', 'description', 'data', 'image', 'subject')
		subject = forms.ModelChoiceField(queryset=Subject.objects.all())
