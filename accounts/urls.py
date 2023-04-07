from django.urls import path
from .views import registerUser, registerVendor, login, logOut, custDashboard, vendorDashboard, myAccount


urlpatterns = [
    path('registerUser/', registerUser, name='registerUser'),
    path('registerVendor/', registerVendor, name='registerVendor'),

    path('login/', login, name="login"),
    path('logOut/', logOut, name="logOut"),
    path('myAccount/', myAccount, name="myAccount"),
    path('custDashboard/', custDashboard, name="custDashboard"),
    path('vendorDashboard/', vendorDashboard, name="vendorDashboard"),
]

