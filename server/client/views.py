from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):
    registration = User.UserManager.valid_registration(request.POST)
    print registration
    if 'user' in registration:
        user = {
            'first_name':registration.user.first_name,
            'user_id':registration.user.id
        }
        return JsonResponse(user)
    else:
        return JsonResponse(registration['messages'])

def getUsers(request):
    return JsonResponse(dict(users = list(User.objects.all())))

@csrf_exempt
def login(request):
    login = User.UserManager.exisiting_user(request.POST):
    if 'user' in login:
        user = { 'user':login.user }
        return JsonResponse(user)
    else:
        return JsonResponse(login['messages'])
