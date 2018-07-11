
from . import views
from django.urls import path,re_path
app_name = "polls"
urlpatterns = [
    path('list/',views.poll_list,name = "polls_list"),
    re_path(r'^$', views.home, name="home"),
    re_path(r'^(?P<id>\d+)/$',views.poll_signle,name="poll_single"),
    re_path(r'^(?P<id>\d+)/voted/$', views.poll_vote ,name= "poll_voted"),
    re_path(r'^list/add$', views.poll_add, name="add"),
    re_path(r'^contact$',views.contact,name="contact"),
    re_path(r'^edit/(?P<id>\d+)/$',views.edit,name = "edit"),
    re_path(r'^edit/(?P<id>\d+)/add_choice/$',views.add_choice,name="add_choice"),
    re_path(r'^edit/choice/(?P<id>\d+)/$',views.edit_choice,name="edit_choice"),
    re_path(r'delete/choice/(?P<id>\d+)/$',views.delete_choice,name ="delete_choice"),
    re_path(r'delete/Poll/(?P<id>\d+)/$',views.delete_poll,name="delete_poll")

]
