from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Review(models.Model):
    host = models.ForeignKey(Host, related_name="host_reviews")
    guest = models.ForeignKey(Guest, related_name="guest_reviews")
    property_review = models.ForeignKey(Property, related_name="property_reviews")
    review_type = models.CharField(max_length=10)
    review = models.TextField()
    star = models.IntegerField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
