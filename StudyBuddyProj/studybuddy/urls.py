from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('mygroups/', views.mygroups, name='mygroups'),
	path('creategroup/', views.creategroup, name='creategroup'),
	url(r'^updategroup_am/(?P<id>[0-9]+)/$', views.updategroup_am, name='updategroup_am'),
	url(r'^updategroup_del/(?P<pk>[0-9]+)/$', views.updategroup_delete, name='updategroup_delete'),
	url(r'^group/(?P<pk>[0-9]+)/$', views.group, name='group'),


]
