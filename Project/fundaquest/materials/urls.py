from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^filecreate/',views.upload_file),
    url(r'^fileview/',views.view_file),


]
