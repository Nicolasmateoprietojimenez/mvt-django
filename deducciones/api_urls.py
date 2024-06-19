# deducciones/api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import PrimaViewSet, SeguridadSocialViewSet, NivelRiesgoViewSet, EmpleadoViewSet

router = DefaultRouter()
router.register(r'primas', PrimaViewSet)
router.register(r'seguridad_social', SeguridadSocialViewSet)
router.register(r'niveles_riesgo', NivelRiesgoViewSet)
router.register(r'empleados', EmpleadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
