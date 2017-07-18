from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthday = models.DateTimeField(max_length=8)
    password = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=10, validators=[phone_regex], blank=True) # validators should be a list
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=30)
    zip_code = models.IntegerField(max_length=10)
    profile_image = models.ImageField(upload_to="profile_pic/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Guest(models.Model):
    user = models.ForeignKey(User, related_name="user_guest")
    about_me = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Host(models.Model):
    user = models.ForeignKey(User, related_name="user_host")
    about_me = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
