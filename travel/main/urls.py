from django.urls import path
from .views import (KlassAPI, KlassDetailAPI, MehmonxonaAPI,
                    MehmonxonaDetailAPI, TravelAPI, TravelDetailAPI)

urlpatterns = [
    path('klass/', KlassAPI.as_view()),
    path('klass/<int:pk>', KlassDetailAPI.as_view()),
    path('mehmonxona/', MehmonxonaAPI.as_view()),
    path('mehmonxona/<int:pk>', MehmonxonaDetailAPI.as_view()),
    path('travel/', TravelAPI.as_view()),
    path('travel/<int:pk>', TravelDetailAPI.as_view()),
]