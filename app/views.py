from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import ApiSerializer, Api


class ApiView (ModelViewSet):
    serializer_class = ApiSerializer
    queryset = Api.objects.all()
    http_method_names = ['get', 'head']
