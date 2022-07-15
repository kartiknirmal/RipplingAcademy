from django.contrib import admin
from django.urls import path

from restaurant import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('getall/', views.get_restaurants, name="get_restaurants"),
    path('create/', views.create_restaurant, name="create_restaurant")
]
