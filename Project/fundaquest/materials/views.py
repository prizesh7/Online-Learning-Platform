from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from .models import File
from subjects.models import Subject

def upload_file(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			#instance = File(file=request.FILES['file'])
			form.save()
			return HttpResponseRedirect('')
	else:
		form = FileForm()
	return render(request, 'materials/file_create.html', {'form': form})

def view_file(request):
	sub=request.GET.get('file')
	print(sub)
	subobj=Subject.objects.filter(subject_name=sub)
	print(subobj)
	file= File.objects.filter(subject__in=subobj)
	print(file)
	return render(request, 'materials/file_view.html', {'file':file})
