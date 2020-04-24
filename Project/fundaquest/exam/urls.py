from django.urls import path
from . import views
from .views import (
    QuestionListView,
    QuestionDetailView,
    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView
)

urlpatterns = [
	path('', QuestionListView.as_view(), name='exam-home'),
    path('question_detail/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question_create/', QuestionCreateView.as_view(), name='question-create'),
	path('question_update/<int:pk>/',QuestionUpdateView.as_view(), name='question-update'),
    path('question_delete/<int:pk>/', QuestionDeleteView.as_view(), name='question-delete'),
]
