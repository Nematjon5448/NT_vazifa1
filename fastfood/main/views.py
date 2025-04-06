from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Burgerlar, Lavashlar, Ichimliklar, Souslar
from .serializers import BurgerlarSerializer, LavashlarSerializer, IchimliklarSerializer, SouslarSerializer

# Burgerlar

class BurgerlarAPI(ListCreateAPIView):
    queryset = Burgerlar.objects.all()
    serializer_class = BurgerlarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BurgerDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Burgerlar.objects.all()
    serializer_class = BurgerlarSerializer
    permission_classes = [permissions.IsAuthenticated]

# Lavashlar

class LavashlarAPI(ListCreateAPIView):
    queryset = Lavashlar.objects.all()
    serializer_class = LavashlarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LavashDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Lavashlar.objects.all()
    serializer_class = LavashlarSerializer
    permission_classes = [permissions.IsAuthenticated]

# Ichimliklar

class IchimliklarAPI(ListCreateAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IchimlikDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    permission_classes = [permissions.IsAuthenticated]

# Souslar

class SouslarAPI(ListCreateAPIView):
    queryset = Souslar.objects.all()
    serializer_class = SouslarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SousDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Souslar.objects.all()
    serializer_class = SouslarSerializer
    permission_classes = [permissions.IsAuthenticated]