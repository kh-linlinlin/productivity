from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^introduction/$', views.introduction, name = 'introduction'),
	url(r'^about/$', views.about, name = "about"),
    url(r'^scan/$', views.ScanView.as_view(), name = 'scan'),
    url(r'^ajax/post/$', views.ScanView.post, name = 'post'),
    url(r'^ajax/modify/(?P<owner>.+)/(?P<modification>.+)/(?P<member>.+)/$', views.modify_grp, name = 'modify_grp'),
    url(r'^ajax/get_user/$', views.get_user_info, name='get_user_info'),
    url(r'^ajax/get_group_members/$', views.get_member_list, name='get_group_mmebers'),
]
 
