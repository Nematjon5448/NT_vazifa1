from django.urls import path

from .views import MuallifDetailAPIView, MuallifAPIView, NashriyotAPIView, NashriyotDetailAPIView, KitobAPIView, \
    KitobDetailAPIView

urlpatterns = [
    path('muallif/', MuallifAPIView.as_view()),
    path('muallif/<int:pk>/', MuallifDetailAPIView.as_view()),
    path('nashriyot/', NashriyotAPIView.as_view()),
    path('nashriyot/<int:pk>', NashriyotDetailAPIView.as_view()),
    path('kitob/', KitobAPIView.as_view()),
    path('kitob/<int:pk>', KitobDetailAPIView.as_view()),
]
