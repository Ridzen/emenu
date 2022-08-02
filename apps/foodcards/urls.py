from django.urls import path

from .views import (PostAPIView, PostRetrieveAPIView, PostCategoriesAPIView, PostCategoryRetrieveAPIView)

urlpatterns = [
    path('33', PostAPIView.as_view()),
    path('<int:pk>/', PostRetrieveAPIView.as_view()),
    path('categories/', PostCategoriesAPIView.as_view()),
    path('categories/<int:pk>/', PostCategoryRetrieveAPIView.as_view()),
]