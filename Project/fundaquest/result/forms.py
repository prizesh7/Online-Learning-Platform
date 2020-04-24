# from django import forms
# from .models import Student,Teacher
# from exam.models import Question
#
#
#
# class QuestionForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Question
# 		fields = ['first_name', 'last_name', 'city', 'dob','phone','department','semester','image']
#
# class TeacherForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Teacher
# 		subject = forms.ModelChoiceField(queryset=Subject.objects.all())
# 		fields = ['first_name', 'last_name', 'phone', 'city','exp','department','image']
