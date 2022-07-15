from rest_framework_mongoengine import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
