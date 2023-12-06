from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('dashboard/', views.dashboard, name='Principal'),
    path('dashboard/data/', views.contenido_datos, name='Datos'),
]
