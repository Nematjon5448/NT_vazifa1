from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Burgerlar, Lavashlar, Ichimliklar, Souslar
from .serializers import BurgerlarSerializer, LavashlarSerializer, IchimliklarSerializer, SouslarSerializer
from .permissions import BurgerPermissions, LavashPermissions, IchimliklarPermissions, SouslarPermissions

# Burgerlar

class BurgerlarAPI(ListCreateAPIView):
    queryset = Burgerlar.objects.all()
    serializer_class = BurgerlarSerializer
    permission_classes = [BurgerPermissions]

class BurgerDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Burgerlar.objects.all()
    serializer_class = BurgerlarSerializer
    permission_classes = [BurgerPermissions]

# Lavashlar

class LavashlarAPI(ListCreateAPIView):
    queryset = Lavashlar.objects.all()
    serializer_class = LavashlarSerializer
    permission_classes = [LavashPermissions]

class LavashDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Lavashlar.objects.all()
    serializer_class = LavashlarSerializer
    permission_classes = [LavashPermissions]

# Ichimliklar

class IchimliklarAPI(ListCreateAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    permission_classes = [IchimliklarPermissions]


class IchimlikDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    permission_classes = [IchimliklarPermissions]

# Souslar

class SouslarAPI(ListCreateAPIView):
    queryset = Souslar.objects.all()
    serializer_class = SouslarSerializer
    permission_classes = [SouslarPermissions]


class SousDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Souslar.objects.all()
    serializer_class = SouslarSerializer
    permission_classes = [SouslarPermissions]