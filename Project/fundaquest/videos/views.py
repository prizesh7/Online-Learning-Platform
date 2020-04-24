from django.shortcuts import render
from django.http import HttpResponseRedirect
from subjects.models import Subject
from .models import Video
from .forms import VideoForm

def upload_video(request):
	if request.method == 'POST':
		form = VideoForm(request.POST, request.FILES)
		if form.is_valid():
			#instance = File(file=request.FILES['file'])
			form.save()
			return render(request, 'users/login_teacher.html')
	else:
		form = VideoForm()
	return render(request, 'videos/video_create.html', {'form': form})

def show_video(request):
    sub=request.GET.get('video')
    subobj=Subject.objects.filter(subject_name=sub)
    lastvideo= Video.objects.filter(subject__in=subobj)
    #video=list(lastvideo)



    return render(request, 'videos/video.html', {'lastvideo':lastvideo})
