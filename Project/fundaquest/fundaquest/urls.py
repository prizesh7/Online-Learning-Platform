"""fundaquest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('home.urls')),
	path('article/', include('articles.urls')),
	path('subject/', include('subjects.subject_urls')),
	path('materials/', include('materials.urls')),
	path('result/', include('result.urls')),
	path('videos/', include('videos.urls')),
	path('faq/', include('faq.urls')),

	path('topic/', include('subjects.topic_urls')),
	path('exam/', include('exam.urls')),
	path('users/', include('users.urls')),
	path('tregister/', user_views.tregister, name='tregister'),
	path('register/', user_views.register, name='register'),
	path('profile/', user_views.profile, name='profile'),
	path('login/', user_views.login, name='login'),
	path('logout/', user_views.logout, name='logout'),
	path('back/', user_views.back, name='back'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
