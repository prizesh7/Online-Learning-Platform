from django.urls import path
from . import views
from .views import (
    SubjectListView,
    SubjectDetailView,
    SubjectCreateView,
    SubjectUpdateView,
    SubjectDeleteView,
    #file
)

urlpatterns = [
	path('all/', SubjectListView.as_view(), name='subjects-home'),
    path('detail/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('create/', SubjectCreateView.as_view(), name='subject-create'),
	path('update/<int:pk>/',SubjectUpdateView.as_view(), name='subject-update'),
    path('delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject-delete'),
	path('file/',views.file)

]
