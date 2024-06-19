from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from . import settings
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', include('login.urls')),
    path('empleados/', include('gestion_empleados.urls')),
    path('devengados/', include('devengos.urls')),
    path('deducciones/', include('deducciones.urls')),
    path('api/', include('deducciones.api_urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
