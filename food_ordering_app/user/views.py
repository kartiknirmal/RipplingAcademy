import json

import certifi
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from item.models import Item
from item.serializers import ItemSerializer
from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = [
        "get-restaurant/",
        "get-items/"
    ]

    return Response(api_urls)

# @api_view(['GET'])
# def get_restaurants_by_name(request, name):
#     try:
#         try:
#             restaurant_by_name = Restaurant.objects(name=name)
#             return Response(RestaurantSerializer(restaurant_by_name, many=True).data, status=200)
#         except Restaurant.DoesNotExist:
#             return Response("No restaurant exist.", status=200)
#
#     except:
#         return Response("Some error occurred", status=500)
#
#
# @api_view(['GET'])
# def get_restaurants_by_cuisines(request, cuisines):
#     try:
#         try:
#             restaurant_by_name = Restaurant.objects(cuisines=cuisines)
#             return Response(RestaurantSerializer(restaurant_by_name, many=True).data, status=200)
#         except Restaurant.DoesNotExist:
#             return Response("No restaurant exist.", status=200)
#
#     except:
#         return Response("Some error occurred", status=500)


# @api_view(['GET'])
# def get_all_available_items_in_restaurant(request, pk):
#     items = Item.objects.filter(restaurant_id=pk, availability__gt=0)
#     serializer = ItemSerializer(items, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def get_items_by_name(request, name):
#     items = Item.objects.filter(name=name, availability__gt=0)
#     serializer = ItemSerializer(items, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def get_restaurants(request):
    if "name" in request.GET and "cuisine" in request.GET:
        name = request.GET["name"]
        cuisines = request.GET["cuisine"]
        try:
            try:
                restaurant = Restaurant.objects(name=name, cuisines=cuisines)
                return Response(RestaurantSerializer(restaurant, many=True).data, status=200)
            except Restaurant.DoesNotExist:
                return Response("No restaurant exist.", status=200)

        except:
            return Response("Some error occurred", status=500)

    elif "name" in request.GET:
        name = request.GET["name"]
        try:
            try:
                restaurant = Restaurant.objects(name=name)
                return Response(RestaurantSerializer(restaurant, many=True).data, status=200)
            except Restaurant.DoesNotExist:
                return Response("No restaurant exist.", status=200)

        except:
            return Response("Some error occurred", status=500)

    elif "cuisine" in request.GET:
        cuisines = request.GET["cuisine"]
        try:
            try:
                restaurant = Restaurant.objects(cuisines=cuisines)
                return Response(RestaurantSerializer(restaurant, many=True).data, status=200)
            except Restaurant.DoesNotExist:
                return Response("No restaurant exist.", status=200)

        except:
            return Response("Some error occurred", status=500)

    else:
        try:
            try:
                restaurant = Restaurant.objects.all()
                return Response(RestaurantSerializer(restaurant, many=True).data, status=200)
            except Restaurant.DoesNotExist:
                return Response("No restaurant exist.", status=200)

        except:
            return Response("Some error occurred", status=500)


@api_view(['GET'])
def get_items(request):
    if "name" in request.GET and "restaurant_id" in request.GET:
        name = request.GET["name"]
        restaurant_id = request.GET["restaurant_id"]
        try:
            try:
                items = Item.objects.filter(name=name, restaurant_id=restaurant_id, availability__gt=0)
                return Response(ItemSerializer(items, many=True).data, status=200)
            except Item.DoesNotExist:
                return Response("No item exist.", status=200)

        except:
            return Response("Some error occurred", status=500)

    elif "name" in request.GET:
        name = request.GET["name"]
        try:
            try:
                items = Item.objects.filter(name=name, availability__gt=0)
                return Response(ItemSerializer(items, many=True).data, status=200)
            except Item.DoesNotExist:
                return Response("No item exist.", status=200)

        except:
            return Response("Some error occurred", status=500)

    elif "restaurant_id" in request.GET:
        restaurant_id = request.GET["restaurant_id"]
        try:
            try:
                items = Item.objects.filter(restaurant_id=restaurant_id, availability__gt=0)
                return Response(ItemSerializer(items, many=True).data, status=200)
            except Item.DoesNotExist:
                return Response("No item exist.", status=200)

        except:
            return Response("Some error occurred", status=500)

    else:
        try:
            try:
                items = Item.objects.filter(availability__gt=0)
                return Response(ItemSerializer(items, many=True).data, status=200)
            except Item.DoesNotExist:
                return Response("No item exist.", status=200)

        except:
            return Response("Some error occurred", status=500)