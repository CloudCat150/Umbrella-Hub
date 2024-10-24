from django.urls import path
from .views import create_rental, rental_confirmation

urlpatterns = [
    path('new/', create_rental, name='create_rental'),  # 대여 등록 페이지
    path('confirmation/<int:pk>/', rental_confirmation, name='rental_confirmation'),  # 확인 페이지
]
