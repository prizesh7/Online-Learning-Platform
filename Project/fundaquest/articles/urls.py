from django.urls import path
from django.conf.urls import url

from . import views
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    

)

urlpatterns = [
	path('', ArticleListView.as_view(), name='articles-home'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
	path('update/<int:pk>/',ArticleUpdateView.as_view(), name='article-update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),

]
