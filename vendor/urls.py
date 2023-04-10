from django.urls import path, include
from .views import vprofile, menu_builder, fooditems_by_category, add_category, edit_category, delete_category
from accounts.views import vendorDashboard


urlpatterns = [
    path('', vendorDashboard, name="vendor"),
    path('profile/', vprofile, name='vprofile'),
    path('menu-builder/', menu_builder, name="menu_builder"),
    path('menu-builder/category/<int:pk>/', fooditems_by_category, name="fooditems_by_category"),

    #Category CRUD
    path('menu-builder/category/add/', add_category, name="add_category"),
    path('menu-builder/category/edit/<int:pk>/', edit_category, name="edit_category"),
    path('menu-builder/category/delete/<int:pk>/', delete_category, name="delete_category"),
]
