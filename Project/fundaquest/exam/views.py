from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Question
from .forms import QuestionForm

class QuestionListView(ListView):
    model = Question
    template_name = 'exam/question_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    #ordering = ['date']

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'exam/question_detail.html'

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'exam/question_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'exam/question_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        return True

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    template_name = 'exam/question_confirm_delete.html'
    success_url = '/exam/'

    def test_func(self):
        question = self.get_object()
        return True
