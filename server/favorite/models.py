from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Favorite(models.Model):
    likes = models.ForeignKey(User, related_name="user_favorites")
    liked = models.ForeignKey(Property, related_name="property_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
