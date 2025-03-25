from django.urls import path
from .views import IndexView, SingleProduct, CommentSaqlash, ShopView, ToCart

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('single_product/<int:product_id>', SingleProduct.as_view(), name='single_product'),
    path('single_product/<int:product_id>/comment', CommentSaqlash.as_view(), name='comment_saqlash'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<slug:category_slug>/', ShopView.as_view(), name='slug_by_category'),
    path('add/product/<slug:product_slug>/<str:action>/', ToCart.as_view(), name='add_to_cart'),

]