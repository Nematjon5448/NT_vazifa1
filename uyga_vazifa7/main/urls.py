from django.urls import path

from .views import (asosiy_sahifa, kitoblar, kitob_haqida, kitob_qoshish, kitob_yangilash,
                    kitob_ochirish, save_comment)

urlpatterns = [
    path('', asosiy_sahifa, name='asosiy_sahifa'),
    path('kitoblar/<int:category_id>', kitoblar, name='kitoblar'),
    path('kitoblar/kitob_haqida/<int:book_id>', kitob_haqida, name='kitob_haqida'),
    path('kitob_qoshish/', kitob_qoshish, name='kitob_qoshish'),
    path('kitoblar/kitob_haqida/<int:book_id>/update', kitob_yangilash, name='kitob_yangilash'),
    path('kitoblar/kitob_haqida/<int:book_id>/delete', kitob_ochirish, name='kitob_ochirish'),
    path('kitoblar/kitob_haqida/<int:book_id>/comment/save', save_comment, name='save_comment')
]