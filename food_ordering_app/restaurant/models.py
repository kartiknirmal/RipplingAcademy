from mongoengine import Document, fields
# Create your models here.


# class Restaurant(models.Model):
#     name = models.CharField()
#     rating = models.FloatField()
#
#     class Meta:
#         app_label = 'restaurant'

class Restaurant(Document):
    name = fields.StringField()
    address = fields.StringField()
    cuisines = fields.ListField()
    rating = fields.FloatField()
