from django.contrib import admin
from django.urls import path

from restaurant import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('getall/', views.get_restaurants, name="get_restaurants"),
    path('create/', views.create_restaurant, name="create_restaurant"),
    path('delete/<pk>', views.delete_restaurant, name="delete_restaurant"),
    path('get/<pk>', views.get_restaurant_by_ID, name="get_restaurant_by_ID")
]
