from django.urls import path
from .views import create_rental, rental_confirmation, RentalListView, mark_as_returned

urlpatterns = [
    path('new/', create_rental, name='create_rental'),  # 대여 등록 페이지
    path('confirmation/<int:pk>/', rental_confirmation, name='rental_confirmation'),  # 확인 페이지
]
from django.urls import path
from .views import 

urlpatterns = [
    path('rentals/', RentalListView.as_view(), name='rental-list'),
    path('rentals/mark_as_returned/<int:rental_id>/', mark_as_returned, name='mark-as-returned'),
]
