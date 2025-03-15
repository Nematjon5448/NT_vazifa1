from django.urls import path
from .views import IndexView, SingleProduct, CommentSaqlash, ShopView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('single_product/<int:product_id>', SingleProduct.as_view(), name='single_product'),
    path('single_product/<int:product_id>/comment', CommentSaqlash.as_view(), name='comment_saqlash'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<slug:category_slug>/', ShopView.as_view(), name='slug_by_category')
]