from django.urls import path
from .views import IndexView, SingleProduct, CommentSaqlash

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('single_product/<int:product_id>', SingleProduct.as_view(), name='single_product'),
    path('single_product/<int:product_id>/comment', CommentSaqlash.as_view(), name='comment_saqlash'),
]