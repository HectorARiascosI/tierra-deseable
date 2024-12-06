from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),  # Verifica que esta URL esté bien configurada
    path('registro/', views.registro_view, name='registro'),
    path('registro-principal/', views.registro_principal_view, name='registro_principal'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Asegúrate de que esta vista exista
]
