from django.urls import path, include
from accounts.views import custDashboard
from .views import cprofile


urlpatterns = [
    path('', custDashboard, name="customer"),
    path('profile/', cprofile, name="cprofile")
]
