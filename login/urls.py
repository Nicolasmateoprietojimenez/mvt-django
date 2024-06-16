from django.urls import path

from login.views import crear_cuenta, login_view, success, verificar_token

urlpatterns = [
    path('register/', crear_cuenta, name='register'),
    path('login/', login_view, name='login'),
    path('success/', success, name='success'),
    path('verificar_token/', verificar_token, name='verificar_token'),
]