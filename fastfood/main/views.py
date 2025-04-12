from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.throttling import AnonRateThrottle
from rest_framework.pagination import CursorPagination

from .models import Burgerlar, Lavashlar, Ichimliklar, Souslar
from .serializers import BurgerlarSerializer, LavashlarSerializer, IchimliklarSerializer, SouslarSerializer
from .permissions import BurgerPermissions, LavashPermissions, IchimliklarPermissions, SouslarPermissions

class FastFoodPagination(CursorPagination):
    ordering = '-name'
    page_size = 2

class BurgerlarThrottle(AnonRateThrottle):
    scope = "burgerlar_list"

class BurgerDetailThrottle(AnonRateThrottle):
    scope = "burger_detail"

class LavashlarThrottle(AnonRateThrottle):
    scope = "lavashlar_list"

class LavashDetailThrottle(AnonRateThrottle):
    scope = "lavash_detail"

class IchimliklarThrottle(AnonRateThrottle):
    scope = "ichimliklar_list"

class IchimlikDetailThrottle(AnonRateThrottle):
    scope = "ichimlik_detail"

class SouslarThrottle(AnonRateThrottle):
    scope = "souslar_list"

class SousDetailThrottle(AnonRateThrottle):
    scope = "sous_detail"

# Burgerlar

class BurgerlarAPI(ListCreateAPIView):
    queryset = Burgerlar.objects.all()
    serializer_class = BurgerlarSerializer
    permission_classes = [BurgerPermissions]
    throttle_classes = [BurgerlarThrottle]

class BurgerDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Burgerlar.objects.all()
    serializer_class = BurgerlarSerializer
    permission_classes = [BurgerPermissions]
    throttle_classes = [BurgerDetailThrottle]

# Lavashlar

class LavashlarAPI(ListCreateAPIView):
    queryset = Lavashlar.objects.all()
    serializer_class = LavashlarSerializer
    permission_classes = [LavashPermissions]
    throttle_classes = [LavashlarThrottle]

class LavashDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Lavashlar.objects.all()
    serializer_class = LavashlarSerializer
    permission_classes = [LavashPermissions]
    throttle_classes = [LavashDetailThrottle]

# Ichimliklar

class IchimliklarAPI(ListCreateAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    permission_classes = [IchimliklarPermissions]
    throttle_classes = [IchimliklarThrottle]


class IchimlikDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    permission_classes = [IchimliklarPermissions]
    throttle_classes = [IchimlikDetailThrottle]

# Souslar

class SouslarAPI(ListCreateAPIView):
    queryset = Souslar.objects.all()
    serializer_class = SouslarSerializer
    permission_classes = [SouslarPermissions]
    throttle_classes = [SouslarThrottle]


class SousDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Souslar.objects.all()
    serializer_class = SouslarSerializer
    permission_classes = [SouslarPermissions]
    throttle_classes = [SousDetailThrottle]