from django.urls import path

from login.views import crear_cuenta, login_view, home_empleados, success, verificar_token

urlpatterns = [
    path('register/', crear_cuenta, name='register'),
    path('login/', login_view, name='login'),
    path('success/', success, name='success'),
    path('empleados/<str:empleado_nro_documento>/', home_empleados, name='home_empleados'),
    path('verificar_token/', verificar_token, name='verificar_token'),
]