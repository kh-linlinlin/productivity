from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^userprofile/$', views.view_profile, name='view_profile'),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    url(r'^userprofile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
]