from django.urls import path

from .views import index_1, index_2, index_3

urlpatterns = [
    path('', index_1),
    path('mualliflar', index_2),
    path('sharhlar', index_3),
]