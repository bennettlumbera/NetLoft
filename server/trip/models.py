from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Trip(models.Model):
    review = models.ForeignKey(Review, related_name="trip_review")
    trip_property = models.ForeignKey(Property, related_name="property_trip")
    guest = models.ForeignKey(Guest, related_name="guest_trip")
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
