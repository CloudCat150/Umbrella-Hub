from django.urls import path
from .views import create_rental, rental_confirmation, RentalListView, mark_as_returned

urlpatterns = [
    path('rentals/new/', create_rental, name='create-rental'),  # 대여 등록 페이지
    path('rentals/confirmation/<int:pk>/', rental_confirmation, name='rental_confirmation'),  # 대여 확인 페이지
    path('rentals/', RentalListView.as_view(), name='rental-list'),  # 대여 목록 페이지
    path('rentals/mark_as_returned/<int:rental_id>/', mark_as_returned, name='mark-as-returned'),  # 반납 처리
]
