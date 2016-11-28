import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from retail.models import Chain, Store, Employee
from retail.serializers import ChainSerializer, StoreSerializer,EmployeeSerializer


class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
