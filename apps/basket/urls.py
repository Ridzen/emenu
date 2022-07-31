from django.urls import path

from .views import (BasketAPIView, BasketRetrieveAPIView)

urlpatterns = [
    path('', BasketAPIView.as_view()),
    path('<int:pk>/', BasketRetrieveAPIView.as_view()),
]