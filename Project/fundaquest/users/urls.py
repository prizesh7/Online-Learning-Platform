from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^sendemails/',views.sendemails),
    url(r'^forgethtml/',views.forgethtml),
    url(r'^forget/',views.forget),
    url(r'^verify/',views.verify),
    url(r'^set/',views.set),
    url(r'^loginstudent/',views.loginstudent),

    # url(r'^snext/',views.studentnext),
    # url(r'^tnext/',views.teachernext),


]
