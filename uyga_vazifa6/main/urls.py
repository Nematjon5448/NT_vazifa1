from django.urls import path

from .views import asosiy_sahifa, add_brand, add_car, update_brand, brand_detail, car_detail, update_car

urlpatterns = [
    path('', asosiy_sahifa, name='home'),
    path('add/brand/', add_brand, name='add_brand'),
    path('brand/<int:brand_id>/update/', update_brand, name='update_brand'),
    path('add/car/', add_car, name='add_car'),
    path('brand/<int:brand_id>/', brand_detail, name='brand_detail'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
    path('car/<int:car_id>/update/', update_car, name='update_car'),
]