from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Subject, Topic
from .forms import SubjectForm, TopicForm

class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/subject_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'subjects'
    ordering = ['-date']

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.filter(subject = context['object'])
        return context

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/subject_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SubjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/subject_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        subject = self.get_object()
        return True

class SubjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subject
    template_name = 'subjects/subject_confirm_delete.html'
    success_url = '/subject/'

    def test_func(self):
        subject = self.get_object()
        return True

class TopicListView(ListView):
    model = Topic
    template_name = 'subjects/topic_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'topics'
    #ordering = ['date']


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'subjects/topic_detail.html'


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'subjects/topic_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TopicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = 'subjects/topic_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        topic = self.get_object()
        return True


class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic
    template_name = 'subjects/topic_confirm_delete.html'
    success_url = '/topic/'

    def test_func(self):
        topic = self.get_object()
        return True

def file(request,subject_name):
    return redirect('/materials/fileview/',{'subject_name':'subject_name'})
