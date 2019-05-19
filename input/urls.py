from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^introduction/$', views.introduction, name = 'introduction'),
	url(r'^about/$', views.about, name = "about"),
    url(r'^scan/$', views.ScanView.as_view(), name = 'scan'),
    url(r'^end/$', views.EndView.as_view(), name = 'end'),
    url(r'^modify/(?P<modification>.+)/(?P<pk>\d+)/$', views.modify_grp, name = 'modify_grp')
]
 
