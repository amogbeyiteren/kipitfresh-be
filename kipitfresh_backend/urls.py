from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blogs.urls')),  # Blog app URLs
    path('api/v1/', include('communication.urls')),  # Communication app URLs
    path('api/', include('pricing.urls')),
]

