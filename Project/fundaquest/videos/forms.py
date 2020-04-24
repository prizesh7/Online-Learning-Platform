
from django import forms
from .models import Video
from users.models import Teacher
from subjects.models import Subject, Topic

class VideoForm(forms.ModelForm):
	class Meta:
		model= Video
		fields= ["topic", "video","teacher","subject"]
		topic = forms.ModelChoiceField(queryset=Topic.objects.all())
		teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
		subject = forms.ModelChoiceField(queryset=Subject.objects.all())


# class VideoForm(forms.ModelForm):
#     class Meta:
#         model= Video
#         fields= ["topic", "video","teacher","subject"]
#         topic = forms.ModelChoiceField(queryset=Topic.objects.all())
# 		teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
# 		subject = forms.ModelChoiceField(queryset=Subject.objects.all())
