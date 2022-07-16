from django.contrib import admin
from django.urls import path

from item import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('create/', views.create_item_for_restaurant, name="create_item_for_restaurant"),
    path('getall/<rk>', views.get_items_for_restaurant, name="get_items_for_restaurant"),
    path('delete/<rk>/<ik>', views.delete_item_for_restaurant, name="delete_item_for_restaurant"),
    path('get/<rk>/<ik>', views.get_item_by_id_for_restaurant, name="get_item_by_id_for_restaurant")
]
