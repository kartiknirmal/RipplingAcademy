import json

import certifi
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer
import pymongo

# client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.id3knfj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
#
# db = client["Food_ordering_db"]
#
# restaurant = db['Restaurant']


@api_view(['GET'])
def api_overview(request):

    return Response("ABCD")


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
        new_restaurant.save()
        return Response("restaurant created", status=200)

    except:
        return Response("All attributes not filled", status=400)
#     new_restaurant = {"name": request.POST['name'], "rating": request.POST['rating']}
#     restaurant.insert_one(new_restaurant)
#
