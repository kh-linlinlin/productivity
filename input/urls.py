from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^api/data/$', views.get_data, name = 'api-data'),
	url(r'^introduction/$', views.introduction, name = 'introduction'),
	url(r'^about/$', views.about, name = "about"),
    url(r'^scan/$', views.ScanView.as_view(), name = 'scan'),
    url(r'^ajax/post/$', views.ScanView.post, name = 'post'),
    url(r'^ajax/record/$', views.ScanView.record, name = 'record'),
    url(r'^ajax/modify/(?P<owner>.+)/(?P<modification>.+)/(?P<member>.+)/$', views.modify_grp, name = 'modify_grp'),
    url(r'^ajax/get_user/$', views.get_user_info, name='get_user_info'),
    url(r'^ajax/get_group_members/$', views.get_member_list, name='get_group_mmebers'),
    url(r'^ajax/check_task/$', views.check_task, name = "check-task"),
]
 
