from django.urls import path
from .views import (CategoryAPIView, CategoryDetailAPIView, ArticleAPIView, ArticleDetailView,
                    CommentAPIView, CommentDetailAPIView)

urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:pk>', ArticleDetailView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:pk>', CommentDetailAPIView.as_view()),
]