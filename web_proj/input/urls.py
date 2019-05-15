from django.urls import path
from . import views
from input.views import ScanView

# home - scan agent barcode - login page
# scan - scan task barcode page
urlpatterns = [
    path('', ScanView.as_view(), name = 'input-scan')
]
 