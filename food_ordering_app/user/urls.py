from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    # path('getname/<name>', views.get_restaurants_by_name, name="get_restaurants_by_name"),
    # path('getcuisine/<cuisines>', views.get_restaurants_by_cuisines, name="get_restaurants_by_cuisines"),
    # path('getitemsinrestaurant/<pk>', views.get_all_available_items_in_restaurant, name="get_all_available_items_in_restaurant"),
    # path('getitems/<name>', views.get_items_by_name, name="get_items_by_name"),
    path('get-restaurant/', views.get_restaurants, name="get_restaurants"),
    path('get-items/', views.get_items, name="get_items")
]
