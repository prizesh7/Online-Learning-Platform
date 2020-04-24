from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Query,Answer
from .forms import QueryForm
from users.models import Teacher
from subjects.models import Subject


class QueryListView(ListView):
	model = Query
	template_name = 'faq/query_home.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'queries'
	#ordering = ['date']


class QueryDetailView(DetailView):
	model = Query
	template_name = 'faq/query_detail.html'


class QueryCreateView(LoginRequiredMixin, CreateView):
	model = Query
	form_class = QueryForm
	template_name = 'faq/query_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class QueryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Query
	form_class = QueryForm
	template_name = 'faq/query_form.html'

	def form_valid(self, form):
		form.instance.student.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		query = self.get_object()
		if self.request.user == query.student.user:
			return True
		return False


class QueryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Query
	template_name = 'faq/query_confirm_delete.html'
	success_url = '/'

	def test_func(self):
		query = self.get_object()
		if self.request.user == query.student.user:
			return True
		return False

def give(request):
	qid=request.GET.get('questionid')
	print(qid)
	q=Query.objects.filter(qid=qid).first()
	print(q)

	return render(request,'faq/textarea.html',{'q':q})



def Ans(request):
	qid=request.POST.get('qid','')
	question=request.POST.get('question','')
	desp=request.POST.get('desp','')
	subject=request.POST.get('subject','')
	print(type(subject))
	user=request.user
	t=Teacher.objects.filter(user=user).first()
	print(t)
	s=Subject.objects.filter(subject_name=subject).first()
	que = Query.objects.filter(qid=qid).first()

	a=Answer(question=que,subject=s,desp=desp,teacher=t)
	a.save()
	return render(request,'faq/textarea.html')

def all(request):
	al=Answer.objects.all()
	all=list(al)
	print(all)
	return render(request,'faq/all.html',{'al':all})
