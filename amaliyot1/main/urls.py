from django.urls import path

from .views import (asosiy_sahifa, BrandBoyichaView, RangBoyichaListView, MashinaBatafsilDetailView, CommentSaqlashView,
                    UserLoginView, UserRegisterView, user_logout, MashinaQoshishCreateView, MashinaUpdateView, MashinaDeleteView, test_index)

urlpatterns = [
    path('', asosiy_sahifa, name='asosiy_sahifa'),
    path('brand/<int:brand_id>/', BrandBoyichaView.as_view(), name='brand_boyicha'),
    path('rang/<int:rang_id>/', RangBoyichaListView.as_view(), name='rang_boyicha'),
    path('mashina/<int:car_id>/', MashinaBatafsilDetailView.as_view(), name='mashina_batafsil'),
    path('mashina/<int:car_id>/comment/saqlash/', CommentSaqlashView.as_view(), name='comment_saqlash'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('add_car/', MashinaQoshishCreateView.as_view(), name='mashina_qoshish'),
    path('mashina/<int:car_id>/update/', MashinaUpdateView.as_view(), name='mashina_yangilash'),
    path('mashina/<int:car_id>/delete/', MashinaDeleteView.as_view(), name='mashina_ochirish')
]