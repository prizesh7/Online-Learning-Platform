from django.urls import path
from . import views
from .views import (
    TopicListView,
    TopicDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView
)

urlpatterns = [
    path('', TopicListView.as_view(), name='topic-list'),
    path('detail/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('create/', TopicCreateView.as_view(), name='topic-create'),
	path('update/<int:pk>/',TopicUpdateView.as_view(), name='topic-update'),
    path('delete/<int:pk>/', TopicDeleteView.as_view(), name='topic-delete'),
]
