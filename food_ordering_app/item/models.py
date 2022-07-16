from django.db import models
from mongoengine import Document, fields
# Create your models here.


class Item(Document):
    name = fields.StringField()
    description = fields.StringField()
    veg = fields.BooleanField()
    category = fields.StringField()
    availability = fields.IntField()
    price = fields.IntField()
    restaurant_id = fields.ObjectIdField()
