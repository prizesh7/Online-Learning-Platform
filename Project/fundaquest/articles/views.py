from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Article
from .forms import ArticleForm


class ArticleListView(ListView):
	model = Article
	template_name = 'articles/article_home.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'articles'
	#ordering = ['date']


class ArticleDetailView(DetailView):
	model = Article
	template_name = 'articles/article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	form_class = ArticleForm
	template_name = 'articles/article_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Article
	form_class = ArticleForm
	template_name = 'articles/article_form.html'

	def form_valid(self, form):
		form.instance.teacher.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		article = self.get_object()
		if self.request.user == article.teacher.user:
			return True
		return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Article
	template_name = 'articles/articles_confirm_delete.html'
	success_url = '/'

	def test_func(self):
		article = self.get_object()
		if self.request.user == article.teacher.user:
			return True
		return False
