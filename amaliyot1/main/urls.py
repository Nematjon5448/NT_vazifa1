from django.urls import path

from .views import asosiy_sahifa, brand_boyicha, rang_boyicha, mashina_batafsil, comment_saqlash, user_login, \
    user_register, user_logout, habar_yuborish, mashina_qoshish

urlpatterns = [
    path('', asosiy_sahifa, name='asosiy_sahifa'),
    path('brand/<int:brand_id>/', brand_boyicha, name='brand_boyicha'),
    path('rang/<int:rang_id>/', rang_boyicha, name='rang_boyicha'),
    path('mashina/<int:car_id>/', mashina_batafsil, name='mashina_batafsil'),
    path('mashina/<int:car_id>/comment/saqlash/', comment_saqlash, name='comment_saqlash'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('send-message/', habar_yuborish, name='habar_yuborish'),
    path('add_car/', mashina_qoshish, name='mashina_qoshish')
]