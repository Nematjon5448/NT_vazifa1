from rest_framework import serializers

from .models import Burgerlar, Lavashlar, Ichimliklar, Souslar

class BurgerlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burgerlar
        fields = '__all__'

class LavashlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lavashlar
        fields = '__all__'

class IchimliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ichimliklar
        fields = '__all__'

class SouslarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souslar
        fields = '__all__'