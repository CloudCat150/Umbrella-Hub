from django.contrib import admin
from django.urls import path
from rental import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/new/', views.create_rental, name='create_rental'),
    path('rental/confirmation/<int:pk>/', views.rental_confirmation, name='rental_confirmation'),
]
