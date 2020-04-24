from django.urls import path
from . import views
from .views import (
    QueryListView,
    QueryDetailView,
    QueryCreateView,
    QueryUpdateView,
    QueryDeleteView
)

urlpatterns = [
	path('', QueryListView.as_view(), name='query-home'),
    path('query_detail/<int:pk>/', QueryDetailView.as_view(), name='query-detail'),
    path('query_create/', QueryCreateView.as_view(), name='query-create'),
	path('query_update/<int:pk>/',QueryUpdateView.as_view(), name='query-update'),
    path('query_delete/<int:pk>/', QueryDeleteView.as_view(), name='query-delete'),
    path('give/', views.give),
    path('all/', views.all),
    path('answer/', views.Ans),

]
