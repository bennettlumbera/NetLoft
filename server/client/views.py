from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):
    registration = User.UserManager.valid_registration(request.POST)
    print registration
    if 'user' in registration:
        user = {
            'first_name': registration["user"]["first_name"],
            'user_id': registration["user"]["id"]
        }
        return JsonResponse(user)
    else:
        return JsonResponse(registration['messages'])

def getUsers(request):
    return JsonResponse(dict(users = list(User.objects.all())))

@csrf_exempt
def login(request):
    login = User.UserManager.existing_user(request.POST)
    if 'user' in login:
        return HttpResponse(serializers.serialize('json', login["user"]), content_type='application/json')
    else:
        return JsonResponse(login['messages'])
