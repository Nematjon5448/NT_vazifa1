from django.urls import path

from .views import asosiy_sahifa, kurs_batafsil, dars_batafsil, comment_saqlash, comment_ochirish, user_login, \
    user_register, comment_yangilash, user_logout

urlpatterns = [
    path('', asosiy_sahifa, name='asosiy_sahifa'),
    path('kurs/<int:kurs_id>/', kurs_batafsil, name='kurs_batafsil'),
    path('kurs/dars/<int:dars_id>/', dars_batafsil, name='dars_batafsil'),
    path('kurs/dars/<int:dars_id>/comment/save/', comment_saqlash, name='comment_saqlash'),
    path('kurs/dars/<int:dars_id>/comment/<int:comment_id>/update/', comment_yangilash, name='comment_yangilash'),
    path('kurs/dars/<int:dars_id>/comment/<int:comment_id>/delete/', comment_ochirish, name='comment_ochirish'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout')
]