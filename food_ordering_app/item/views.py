import json

import certifi
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from item.models import Item
from item.serializers import ItemSerializer

# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls=[
        "create/",
        "getall/<rk>",
        "delete/<rk>/<ik>",
        "get/<rk>/<ik>"
    ]

    return Response(api_urls)


@api_view(['POST'])
def create_item_for_restaurant(request):
    try:
        new_item = Item()
        params = json.loads(request.body)
        new_item.name = params['name']
        new_item.description = params["description"]
        new_item.veg = params["veg"]
        new_item.category = params["category"]
        new_item.availability = params["availability"]
        new_item.price = params["price"]
        new_item.restaurant_id = params["restaurant_id"]
        rest_id = new_item.save().id
        return Response("Item created with id {}".format(rest_id), status=200)

    except:
        return Response("All attributes not filled", status=400)


@api_view(['GET'])
def get_items_for_restaurant(request, rk):
    items = Item.objects(restaurant_id=rk)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_item_for_restaurant(request, rk, ik):
    Item.objects(restaurant_id=rk, id=ik).delete()
    return Response("Item Deleted successfully")


@api_view(['GET'])
def get_item_by_id_for_restaurant(request, rk, ik):
    try:
        try:
            item_by_ID = Item.objects.get(id=ik, restaurant_id=rk)
            return Response(ItemSerializer(item_by_ID, many=False).data, status=200)
        except Item.DoesNotExist:
            return Response("No such item exist.", status=200)

    except:
        return Response("Some error occurred", status=500)


