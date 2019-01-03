from django.urls import re_path

from . import views

app_name = "awards"
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^crimes/$', views.crimes, name='crimes'),
    re_path(r'^drugs/$', views.drugs, name='drugs'),

    re_path(r'^updateKey/$', views.updateKey, name='updateKey'),
    re_path(r'^logout/$', views.logout, name='logout'),

    # path('<int:tId>', views.details, name='details'),
    ]