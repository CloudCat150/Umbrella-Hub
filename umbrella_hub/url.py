from django.contrib import admin
from django.urls import path
from rental import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rentals/new/', views.create_rental, name='create_rental'),
    path('rentals/confirmation/<int:pk>/', views.rental_confirmation, name='rental_confirmation'),
    path('rentals/', views.RentalListView.as_view(), name='rental-list'),  # 대여 목록 페이지
    path('rentals/mark_as_returned/<int:rental_id>/', views.mark_as_returned, name='mark-as-returned'),  # 반납 처리
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)