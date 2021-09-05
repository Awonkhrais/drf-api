from django.shortcuts import render
from .models import CurveCoffee
from rest_framework import generics
from .serializers import CurveCoffeSerializer


# Create your views here.

class CoffeeListView(generics.ListCreateAPIView):
    queryset = CurveCoffee.objects.all()
    serializer_class = CurveCoffeSerializer


class CoffeeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurveCoffee.objects.all()
    serializer_class = CurveCoffeSerializer