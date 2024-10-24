# umbrella_hub/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/', include('rental.urls')),  # 'rental/' 앱의 URL을 포함
]
