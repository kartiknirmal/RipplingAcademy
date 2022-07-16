import json

import certifi
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from item.models import Item
from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer

# Create your views here.

import pymongo

# client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.id3knfj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
#
# db = client["Food_ordering_db"]
#
# restaurant = db['Restaurant']


@api_view(['GET'])
def api_overview(request):
    api_urls=[
        "getall/",
        "create/",
        "delete/<pk>",
        "get/<pk>"
    ]

    return Response(api_urls)


@api_view(['GET'])
def get_restaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_restaurant(request):
    try:
        new_restaurant = Restaurant()
        params = json.loads(request.body)
        new_restaurant.name = params['name']
        new_restaurant.rating = params["rating"]
        new_restaurant.cuisines = params["cuisines"]
        new_restaurant.address = params["address"]
        rest_id = new_restaurant.save().id
        return Response("restaurant created with id {}".format(rest_id), status=200)

    except:
        return Response("All attributes not filled", status=400)


@api_view(['DELETE'])
def delete_restaurant(request, pk):
    Item.objects(restaurant_id=pk).delete()
    Restaurant.objects(id=pk).delete()
    return Response("Restaurant Deleted successfully")


@api_view(['GET'])
def get_restaurant_by_ID(request, pk):
    try:
        try:
            restaurant_by_ID = Restaurant.objects.get(id=pk)
            return Response(RestaurantSerializer(restaurant_by_ID, many=False).data, status=200)
        except Restaurant.DoesNotExist:
            return Response("No such restaurant exist.", status=200)

    except:
        return Response("Some error occurred", status=500)






