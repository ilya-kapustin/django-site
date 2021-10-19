from django.urls import path
from .api_views import ShopsGroupListAPIView, ShopsListAPIView

urlpatterns = [
    path('categories/', ShopsGroupListAPIView.as_view(), name='categories'),
    path('goods/', ShopsListAPIView.as_view(), name='goods'),
]