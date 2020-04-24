from django import forms
from .models import Article
from users.models import Teacher
from subjects.models import Subject, Topic

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('topic', 'data', 'teacher', 'subject')
		topic = forms.ModelChoiceField(queryset=Topic.objects.all())
		teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
		subject = forms.ModelChoiceField(queryset=Subject.objects.all())
