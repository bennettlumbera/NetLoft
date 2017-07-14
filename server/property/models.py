from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Property(models.Model):
    owner = models.ForeignKey(Host, related_name="host_properties")
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField(max_length=30)
    property_type = models.CharField(max_length=12)
    rental_type = models.CharField(max_length=20)
    house_rules = models.TextField()
    cancellation_policy = models.CharField(max_length=10)
    amenities = models.TextField()
    number_of_bedrooms = models.IntegerField(max_length=2)
    number_of_bathrooms = models.IntegerField(max_length=2)
    accommdates = models.IntegerField(max_length=2)
    times_viewed = models.IntegerField(max_length=4)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

class Property_Image(models.Model):
    caption = models.CharField(max_length=40)
    image = ImageField(upload_to="property_images/", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
