from django.shortcuts import render,redirect
from .forms import SearchForm
from articles.models import Article

def home(request):
	form = SearchForm()
	return render(request, 'home/home.html', {'form':form})

def search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			searchtext = form.cleaned_data.get('q')
		articles = Article.objects.all()

		for article in articles:
			articlelist = []
			if searchtext in article.topic.topic_name + article.data + article.teacher.first_name + article.teacher.last_name + article.subject.subject_name:
				articlelist.append(articles)
				return redirect('/article', {'articlelist': articlelist })
	return redirect('/article')

def about(request):
	return render(request, 'home/about.html')
