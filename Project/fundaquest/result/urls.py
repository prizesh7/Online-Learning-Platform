from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^take/',views.take),
    url(r'^verify/',views.verify),

]
