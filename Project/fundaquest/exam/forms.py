from django import forms
from users.models import Teacher
from subjects.models import Subject
from .models import Question

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question', 'opt1', 'opt2', 'opt3','opt4', 'answer', 'hint', 'marks', 'difficulty', 'teacher', 'subject')
		teacher = Teacher.objects.all()
		subject = Subject.objects.all()
