from django.urls import path
from . import views

# home - scan agent barcode - login page
# scan - scan task barcode page
urlpatterns = [
    path('', views.home, name = 'scan-home'),
    path('', views.about, name = 'input-about'),
]
 