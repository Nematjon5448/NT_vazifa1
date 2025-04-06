from django.urls import path

from .views import (BurgerlarAPI, BurgerDetailAPI, LavashlarAPI, LavashDetailAPI, IchimliklarAPI,
                    IchimlikDetailAPI, SouslarAPI, SousDetailAPI)

urlpatterns = [
    path('burgerlar/', BurgerlarAPI.as_view()),
    path('burgerlar/<int:pk>', BurgerDetailAPI.as_view()),

    path('lavashlar/', LavashlarAPI.as_view()),
    path('lavashlar/<int:pk>', LavashDetailAPI.as_view()),

    path('ichimliklar/', IchimliklarAPI.as_view()),
    path('ichimliklar/<int:pk>', IchimlikDetailAPI.as_view()),

    path('souslar/', SouslarAPI.as_view()),
    path('souslar/<int:pk>', SousDetailAPI.as_view()),
]