from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home-home'),
	path('search/', views.search, name='home-search'),
	path('about/', views.about, name='home-about'),
]