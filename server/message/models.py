from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.TextField()
    date = models.DateTimeField()
    guest = models.ForeignKey(Guest, related_name="guest_messages")
    host = models.ForeignKey(Host, related_name="host_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
